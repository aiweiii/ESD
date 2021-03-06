# ESD with Love

## About our Project
Our application is an ecommerce platform that holds many sellers, offering users a wide range of items and vendors to purchase from. <br>In our project, the user scenarios we are covering includes adding items to cart by user, purchase of items, and option to cancel order before it has been shipped out.


### Architecture
It uses Kong API Gateway:
* Entry point for client to make API requests. Kong will route incoming client requests to the relevant services (final API)

It uses 1 composite microservice:
* Place Order
  <br>Make calls to all the required microservices, consolidate the data, and transform the data before sending it to UI. 

It uses 7 microservices:
* Customer to handle customer data.
* Seller to handle seller data.
* Inventory to handle products.
* Cart to handle items in cart.
* Order to process orders.
* Notification to notify sellers on order cancellation.
* Activity Log to record order cancellation.

## Technologies

* Docker to package and run microservices in containers. Applications are run using Docker compose.
* SpringBoot enables building production-ready applications quickly and provides non-functional features
* SQLAlchemy to  to execute raw SQL statements using Python
* Flask to build a web application using Python
* RabbitMQ as message broker to reduce loads and delivery times taken by web application servers
* Kong to manage communication between client and various microservices via API


## How to run

1. Download WAMP/MAMP. Set MySQL Port to 8080. Start WAMP/MAMP.
2. On browser, go to http://localhost/phpmyadmin/ to check connection with database
3. Start Docker
4. Clone project
5. cd into ESD/Compiled/project
6. On Terminal, run docker-compose build.
7. On Terminal, run docker-compose up.
8. On another terminal, cd into ESD/UI
9. On Terminal, run python3 app.py

