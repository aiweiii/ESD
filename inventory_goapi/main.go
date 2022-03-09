package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"time"

	_ "github.com/go-sql-driver/mysql"

	"net/http"

	"github.com/gorilla/mux"
	"github.com/jinzhu/gorm"

	// "database"
	"encoding/json"
	"io/ioutil"
	// error creation method:
	// "errors"
)

// SET THESE VARIABLES FOR DATABASE CONNECTION:
const (
	username = "springuser"
	password = "password"

	// for localhost development using MAMP, uncomment this:
	// hostname = "localhost:3306"

	// // for docker mysql developement, uncomment this:
	hostname = "docker-mysql:3306"

	// name of db u would like created:
	dbname = "M"
)

func dsn(dbName string) string {
	return fmt.Sprintf("%s:%s@tcp(%s)/%s", username, password, hostname, dbName)
}

func dbConnection() (*sql.DB, error) {
	db, err := sql.Open("mysql", dsn(""))
	// dont handle the error here:
	if err != nil {
		log.Printf("Error %s when opening DB\n", err)
		return nil, err
	}
	//defer db.Close()

	ctx, cancelfunc := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancelfunc()
	res, err := db.ExecContext(ctx, "CREATE DATABASE IF NOT EXISTS "+dbname)
	if err != nil {
		log.Printf("Error %s when creating DB\n", err)
		return nil, err
	}
	no, err := res.RowsAffected()
	if err != nil {
		log.Printf("Error %s when fetching rows", err)
		return nil, err
	}
	log.Printf("rows affected %d\n", no)

	db.Close()
	db, err = sql.Open("mysql", dsn(dbname))
	if err != nil {
		log.Printf("Error %s when opening DB", err)
		return nil, err
	}
	//defer db.Close()
	db.SetMaxOpenConns(20)
	db.SetMaxIdleConns(20)
	db.SetConnMaxLifetime(time.Minute * 5)

	ctx, cancelfunc = context.WithTimeout(context.Background(), 5*time.Second)
	defer cancelfunc()
	err = db.PingContext(ctx)
	if err != nil {
		log.Printf("Errors %s pinging DB", err)
		return nil, err
	}
	log.Printf("Connected to DB %s successfully\n", dbname)
	return db, nil
}

func createProductTable(db *sql.DB) error {
	// edit the table you wanna create:
	query := `CREATE TABLE IF NOT EXISTS product(product_id int primary key auto_increment, product_name text, 
        product_price int, created_at datetime default CURRENT_TIMESTAMP, updated_at datetime default CURRENT_TIMESTAMP)`
	ctx, cancelfunc := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancelfunc()
	res, err := db.ExecContext(ctx, query)
	if err != nil {
		log.Printf("Error %s when creating product table", err)
		return err
	}
	rows, err := res.RowsAffected()
	if err != nil {
		log.Printf("Error %s when getting rows affected", err)
		return err
	}
	log.Printf("Rows affected when creating table: %d", rows)
	return nil
}

// --------------------------------NEW TUTORIAL STUFF------------------
// CLIENT PART:
//Connector variable used for CRUD operation's
var Connector *gorm.DB

//Connect creates MySQL connection
func Connect(connectionString string) error {
	var err error
	Connector, err = gorm.Open("mysql", connectionString)
	Connector, _ = gorm.Open("mysql", connectionString)
	// // dont handle the error -- so dcoker will keep restarting upon error:
	if err != nil {
		return err
	}
	log.Println("Connection was successful!!")
	return nil
}

// CONFIG PART:

//Config to maintain DB configuration properties
type Config struct {
	ServerName string
	User       string
	Password   string
	DB         string
}

var getConnectionString = func(config Config) string {
	connectionString := fmt.Sprintf("%s:%s@tcp(%s)/%s?charset=utf8mb4&collation=utf8mb4_unicode_ci&parseTime=true&multiStatements=true", config.User, config.Password, config.ServerName, config.DB)
	return connectionString
}

// type Person2 struct {
// 	ID        string `json:"id"`
// 	FirstName string `json:"firstName"`
// 	LastName  string `json:"lastName"`
// 	Age       string `json:"age"`
// 	}

type Item struct {
	ID          int    `json:"id"`
	ProductName string `json:"name"`
	Quantity    int    `json:"quantity"`
}

func createItem(w http.ResponseWriter, r *http.Request) {
	requestBody, _ := ioutil.ReadAll(r.Body)
	var item Item
	json.Unmarshal(requestBody, &item)

	Connector.Create(item)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(item)
}

func getItemByID(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	key := vars["id"]

	var item Item
	Connector.First(&item, key)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(item)
}

func helloFn(w http.ResponseWriter, r *http.Request) {
	// vars := mux.Vars(r)
	// key := vars["id"]

	// var item Item
	// Connector.First(&item, key)
	// w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode("helllooooo")
}

//Migrate create/updates database table
func Migrate(table *Item) {
	Connector.AutoMigrate(&table)
	log.Println("Table migrated")
}

func main() {
	db, error_ := dbConnection()
	if error_ != nil {
		log.Printf("Error %s when getting db connection", error_)
		return
	}
	defer db.Close()
	log.Printf("Successfully connected to database")
	// err = createProductTable(db)
	// if err != nil {
	//     log.Printf("Create product table failed with error %s", err)
	//     return
	// }

	config :=
		Config{
			ServerName: hostname,
			User:       username,
			Password:   password,
			DB:         dbname,
		}

	connectionString := getConnectionString(config)
	err := Connect(connectionString)
	if err != nil {
		panic(err.Error())
	}

	Migrate(&Item{})

	log.Println("Starting the HTTP server on port 9090")
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/create", createItem).Methods("POST")
	router.HandleFunc("/get/{id}", getItemByID).Methods("GET")
	router.HandleFunc("/", helloFn).Methods("GET")
	log.Fatal(http.ListenAndServe(":9090", router))

}
