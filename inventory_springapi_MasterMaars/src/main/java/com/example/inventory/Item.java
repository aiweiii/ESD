package com.example.inventory;


import javax.persistence.Entity;
//import javax.persistence.GeneratedValue;
//import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Item {


//    type Item struct {
//        ID          int    `json:"id"`
//        ProductName string `json:"name"`
//        Quantity    int    `json:"quantity"`
//    }
    @Id
    private int ID;
    private String productName;
    private int quantity;
    private int sellerId;

    Item(int ID, String productName, int quantity, int sellerId){
        this.ID = ID;
        this.productName = productName;
        this.quantity = quantity;
        this.sellerId = sellerId;
    }

    Item(){}

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }






}
