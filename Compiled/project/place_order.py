from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ
import requests
from pathlib import Path

if Path('invokes.py').is_file():
    print ("invokes.py File existssss!!!!")
else:
    print ("invokes.py File not exist")

if Path('amqp_setup.py').is_file():
    print ("amqp_setup.py file existssss!!!!")
else:
    print ("amqp_setup.py file not exist")

from invokes import invoke_http
# try:
#     f = open("invokes.py")
#     # Do something with the file
# except IOError:
#     print("File not accessible")
# finally:
#     f.close()

# cache


import amqp_setup
import pika
import json





app = Flask(__name__)
CORS(app)



# official URLS USED:




# SCHOOL ONES:
#book_URL = "http://localhost:5000/book"
order_URL = "http://localhost:5001/order"
shipping_record_URL = "http://localhost:5002/shipping_record"
#activity_log_URL = "http://localhost:5003/activity_log"
#error_URL = "http://localhost:5004/error"


# SUPPORTED_HTTP_METHODS = set([
#     "GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"
# ])

# def invoke_http(url, method='GET', json=None, **kwargs):

    # print(f"invoke_http json: {json}")
    # """A simple wrapper for requests methods.
    #    url: the url of the http service;
    #    method: the http method;
    #    data: the JSON input when needed by the http method;
    #    return: the JSON reply content from the http service if the call succeeds;
    #         otherwise, return a JSON object with a "code" name-value pair.
    # """
    # code = 200
    # result = {}

    # try:
    #     if method.upper() in SUPPORTED_HTTP_METHODS:
    #         r = requests.request(method, url, json = json, **kwargs)
    #     else:
    #         raise Exception("HTTP method {} unsupported.".format(method))
    # except Exception as e:
    #     code = 500
    #     result = {"code": code, "message": "invocation of service fails: " + url + ". " + str(e)}
    # if code not in range(200,300):
    #     return result

    # ## Check http call result
    # if r.status_code != requests.codes.ok:
    #     code = r.status_code
    # try:
    #     result = r.json() if len(r.content)>0 else ""
    # except Exception as e:
    #     code = 500
    #     result = {"code": code, "message": "Invalid JSON output from service: " + url + ". " + str(e)}

    # return result


# CARTURL = "http://localhost:9393/"
# INVENTORYURL = "http://localhost:9090/"
# CUSTOMERURL = "http://localhost:9292/"
# SELLERURL = "http://localhost:9191/"
# ORDERURL = "http://localhost:5001/" + "order"


# CARTURL = "http://host.docker.internal:9393/"
# INVENTORYURL = "http://host.docker.internal:9090/"
# CUSTOMERURL = "http://host.docker.internal:9292/"
# SELLERURL = "http://host.docker.internal:9191/"
# ORDERURL = "http://host.docker.internal:9494/" + "order"



# print("ALL PRESENT:")
# print(f"CARTURL: {environ.get('CARTURL')}")
# print(f"INVENTORYURL: {environ.get('INVENTORYURL')}")
# print(f"CUSTOMERURL: {environ.get('CUSTOMERURL')}")
# print(f"SELLERURL: {environ.get('SELLERURL')}")
# print(f"ORDERURL: {environ.get('ORDERURL')}")


CARTURL = environ.get('CARTURL')
INVENTORYURL = environ.get('INVENTORYURL')
CUSTOMERURL = environ.get('CUSTOMERURL')
SELLERURL = environ.get('SELLERURL')
ORDERURL = environ.get('ORDERURL') + "order"




def getAllCartItems(customerId):
    url = CARTURL + "cart/" + str(customerId)
    response = requests.request("GET", url, headers={}, data={}).json()
    print(f"cart response: {response}  \n")
    return response


def deleteCustomerCart(customerId):
    url = CARTURL + "/deleteCart/" + customerId
    response = requests.request("DELETE", url, headers={}, data={})
    print(f"cart response: {response}  \n")
    return response



def getAllInventoryItems(itemId):
    url = INVENTORYURL + "items/" + str(itemId)
    response = requests.request("GET", url, headers={}, data={}).json()
    return response


def getCustomerInfo(customerId):
    url = CUSTOMERURL + "customers/" +  str(customerId)
    response = requests.request("GET", url, headers={}, data={}).json()
    print(f"customer response: {response}  \n")
    return response

def getSellerInfo(sellerId):
    # current route for getting seller info:
    url = SELLERURL + "sellers/" + str(sellerId)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).json()
    print(f"seller response: {response} \n")
    return response

# def getPaymentConfirmation():

@app.route("/place_order", methods=['POST'])
def place_order():
    # Simple check of input format and data of the request are JSON

    # assuming customer id sent from frontend: -- > 1
    custId = 2


    # print(f"the order is going to look like thisssss: {order} ")
    # print()
    # print(f"request: {request}")

    if request.is_json:
        try:
            custId = str(request.get_json()["customer_id"])
            print(f"custId2: {custId}")
            requestedCartItems = getAllCartItems(custId)

        # checking if item in cart is available in inventory:
            cart_item = []
            for i in requestedCartItems:
                itemInfo = getAllInventoryItems(i["itemId"])
                print(f"itemInfo fetched: {itemInfo}")
                cartObj = {"itemId": itemInfo["id"],
                    "itemName": itemInfo["productName"],
                    "itemQuantity": itemInfo["quantity"],
                    "sellerId": itemInfo["sellerId"],
                    "itemPrice": itemInfo["itemPrice"],}

                cartObjType = {"itemId": type(itemInfo["id"]),
                    "itemName": type(itemInfo["productName"]),
                    "itemQuantity": type(itemInfo["quantity"]),
                    "sellerId": type(itemInfo["sellerId"]),}

                print(f"cartObjType: {cartObjType}")

                cart_item.append(cartObj)
                print("")
                print("")

            print(f"endResultObjects: {cart_item}")

            customerInfo = getCustomerInfo(custId)

            print("")

            if customerInfo['code'] != 200 or len(requestedCartItems) == 0:
                return { "code": 400, "msg": "invalid fetching of data from one of the three databases"}

            order = {
            "customer_id": custId,
            "cart_item": cart_item
            }

            order = {
                "customer_id": custId,
                "cart_item": cart_item,
                "status": "PaymentCompleted"
            }


            print("\nReceived an order in JSON:", order)

            # do the actual work
            # 1. Send order info {cart items}

            order = json.dumps(order)
            print(f"order jsondumped: {order}")

            result = processPlaceOrder(order, custId)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "place_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

# @app.route("/after_paymentSuccess", methods=['POST'])
def processPlaceOrder(order, custId):
    # 2. Send the order info {cart items}
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    headers = {
    'Content-Type': 'application/json'
    }
    # problem here:
    # invoke_http(url, method='GET', json=None, **kwargs):
    print(f"ORDERURL: {ORDERURL} \n")
    order_result = invoke_http(ORDERURL, method='POST', json=order)
    print(f"order_result: {order_result}")
    code = order_result["code"]
    message = json.dumps(order_result)

    if code not in range(200, 300):
        # Inform the error microservice
        #print('\n\n-----Invoking error microservice as order fails-----')
        print('\n\n-----Publishing the (order error) message with routing_key=order.error-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        # make message persistent within the matching queues until it is received by some receiver 
        # (the matching queues have to exist and be durable and bound to the exchange)

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
        print("\nOrder status ({:d}) published to the RabbitMQ Exchange:".format(
            code), order_result)

        # 7. Return error
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Order creation failure sent for error handling."
        }

    # Notice that we are publishing to "Activity Log" only when there is no error in order creation.
    # In http version, we first invoked "Activity Log" and then checked for error.
    # Since the "Activity Log" binds to the queue using '#' => any routing_key would be matched 
    # and a message sent to “Error” queue can be received by “Activity Log” too.

    else:
        # 4. Record new order
        # record the activity log anyway
        print('\n\n-----Clearing items from CART of customer-----')
        
        deleteCustomerCart(custId)

        print('\n\n-----Publishing the (order info) message with routing_key=order.info-----')        

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.info", 
            body=message)
    
    print("\nOrder published to RabbitMQ Exchange.\n")

    
    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "order_result": order_result
        
        }
    }


# splitting shipping order up:

@app.route("/processShipping/<string:order_id>")
def shippingInvoke(order_id):
    # 5. Send new order to shipping
    # Invoke the shipping record microservice
    print('\n\n-----Invoking processShipping-----')    
    

    shippedStatusChange = invoke_http(ORDERURL + "/" + order_id, method='PUT', json={"status": "Shipped"})

    print('\n\n-----Can check if shipped status update-----')    

    # Check the shipping result;
    # if a failure, send it to the error microservice.
    code = shippedStatusChange["code"]
    if code not in range(200, 300):
        # Inform the error microservice
        #print('\n\n-----Invoking error microservice as shipping fails-----')
        print('\n\n-----Publishing the (shipping error) message with routing_key=shipping.error-----')

        # invoke_http(error_URL, method="POST", json=shipping_result)
        message = json.dumps(shippedStatusChange)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="shipping.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))

        print("\nShipping status ({:d}) published to the RabbitMQ Exchange:".format(
            code), shippedStatusChange)

        # 7. Return error
        return {
            "code": 400,
            "data": {
                "order_result": order_id,
                "shipping_result": shippedStatusChange
            },
            "message": "Simulated shipping record error sent for error handling."
        }

    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "order_result": order_id,
            "shipping_result": shippedStatusChange
        }
    }

@app.route("/cancelOrder", methods=['POST'])
def processCancelOrder():


    if request.is_json:
        try:
            order = request.get_json()
            print("\nReceived an order in JSON:", order)

            # do the actual work
            # 1. Send order info {cart items}
            result = processCancelOrder(order)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "place_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400




def processCancelOrder(order):
    # 2. Send the order info {cart items}
    # Invoke the order microservice
    print('\n-----Invoking order cancel microservice-----')

    # problem here:
    # order_result = invoke_http(order_URL, method='POST', json=order)

    
    order_data = invoke_http(ORDERURL + "/" + str(order["id"]), method='GET')
    print(f"got the cancelled order_data: {order_data}")


    print(f"order_result being cancelled: {order_data} \n")
    orderItemSellers = []
    # # for i in order_result["data"]["order_result"]["data"]["order_item"]
    items = order_data["data"]["order_item"]
    print(f"\n\n\nitems cancelled list: {items} \n")

    for item in items:
        # shd call selller api to get chat id!:
        # {'lliqing': 202631841, 'maars505': 493366384}
        chatdict = {1: "493366384", 2: "202631841", }

        orderItemSellers += [str(chatdict[item["sellerID"]])]


    # if status is already cancelled or it has been shipped, make it unable to cancel:
    if order_data["data"]["status"] != "PaymentCompleted":
        return {
            "code": 500,
            "data": {"order_result": order_data},
            "message": "Order cancellation failure as order has been shipped or already cancelled and cannot be cancelled"
        }

    order_result = invoke_http(ORDERURL + "/" + str(order["id"]), method='PUT', json={"status": "Cancelled"})
    

    print('order_result:', order_result)

    # Check the order result; if a failure, send it to the error microservice.
    code = order_result["code"]
    # message = json.dumps(order_result)
    message = {'code': 201, 'data': "#".join(orderItemSellers)}
    print(f"message sent to amqp for cancelorder: {message}")
    # code = message["code"]
    print(f"actual code issss: {code}")

    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Publishing the (order error) message with routing_key=order.error-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        

        print("\nOrder new cancelled status ({:d}) published to the RabbitMQ Exchange:".format(
            code), order_result)

        # 7. Return error
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Order creation failure sent for error handling."
        }


    else:

        print('\n\n-----Cancelled the (order info) message with routing_key=order.info-----')   
        # {'code': 201, 'data': 21}     

        allSellers = '#'.join(orderItemSellers)
        print(f"allSellers sent to queue: {allSellers}")
        message = {}
        # message['teleSeller'] = allSellers
        message['code'] = 201
        message['data'] = allSellers
        message['teleSeller'] = allSellers
        message["allInfo"] = order_result

        # organise by seller:
        
        print(f"valid tele message for publishing: {message}")
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.info", 
            body=message)

    print("\nOrder published to RabbitMQ Exchange.\n")
    return {
        "code": 201,
        "data": {
            "order_result": order_result
            # "shipping_result": shippedStatusChange

        },
        "message": "Order has been cancelled!"
    }




# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    # print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # app.run(port=5100, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
