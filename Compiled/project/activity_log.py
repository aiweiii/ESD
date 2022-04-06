#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import json
# import os
from flask import Flask, request, jsonify
import requests
# telegram imports:
# from sendTeleUpdate import messageTele

# from pathlib import Path
# if Path('amqp_setup.py').is_file():
#     print ("amqp_setup.py file existssss!!!!")
# else:
#     print ("amqp_setup.py file not exist")

from os import environ

# SELLERURL = "http://localhost:9191/"
SELLERURL = environ.get('SELLERURL')

import amqp_setup



# # -------------------------------------------------------- AMQP STUFFFFF:   -------------------------------------------------------- 



# import pika

# # These module-level variables are initialized whenever a new instance of python interpreter imports the module;
# # In each instance of python interpreter (i.e., a program run), the same module is only imported once (guaranteed by the interpreter).

# # hostname = "localhost" # default hostname
# hostname = "host.docker.internal:5672"
# port = 5672 # default port
# # connect to the broker and set up a communication channel in the connection
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(
#         host=hostname, port=port,
#         heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
# ))
#     # Note about AMQP connection: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
#     # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls.
#     # If see: Stream connection lost: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)
#     # - Try: simply re-run the program or refresh the page.
#     # For rare cases, it's incompatibility between RabbitMQ and the machine running it,
#     # - Use the Docker version of RabbitMQ instead: https://www.rabbitmq.com/download.html
# channel = connection.channel()
# # Set up the exchange if the exchange doesn't exist
# # - use a 'topic' exchange to enable interaction
# exchangename="order_topic"
# exchangetype="topic"
# channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)
#     # 'durable' makes the exchange survive broker restarts

# # Here can be a place to set up all queues needed by the microservices,
# # - instead of setting up the queues using RabbitMQ UI.

# ############   Error queue   #############
# #delcare Error queue
# queue_name = 'Error'
# channel.queue_declare(queue=queue_name, durable=True) 
#     # 'durable' makes the queue survive broker restarts

# #bind Error queue
# channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.error') 
#     # bind the queue to the exchange via the key
#     # any routing_key with two words and ending with '.error' will be matched

# ############   Activity_Log queue    #############
# #delcare Activity_Log queue
# queue_name = 'Activity_Log'
# channel.queue_declare(queue=queue_name, durable=True)
#     # 'durable' makes the queue survive broker restarts

# #bind Activity_Log queue
# channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='#') 
#     # bind the queue to the exchange via the key
#     # 'routing_key=#' => any routing_key would be matched
    


# ############   Activity_Log queue    #############
# #delcare Activity_Log queue
# queue_name = 'OrderCancellation'
# channel.queue_declare(queue=queue_name, durable=True)
#     # 'durable' makes the queue survive broker restarts

# #bind Activity_Log queue
# channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.cancel') 
#     # bind the queue to the exchange via the key
#     # 'routing_key=#' => any routing_key would be matched
    

# """
# This function in this module sets up a connection and a channel to a local AMQP broker,
# and declares a 'topic' exchange to be used by the microservices in the solution.
# """
# def check_setup():
#     # The shared connection and channel created when the module is imported may be expired, 
#     # timed out, disconnected by the broker or a client;
#     # - re-establish the connection/channel is they have been closed
#     global connection, channel, hostname, port, exchangename, exchangetype

#     if not is_connection_open(connection):
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
#     if channel.is_closed:
#         channel = connection.channel()
#         channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)


# def is_connection_open(connection):
#     # For a BlockingConnection in AMQP clients,
#     # when an exception happens when an action is performed,
#     # it likely indicates a broken connection.
#     # So, the code below actively calls a method in the 'connection' to check if an exception happens
#     try:
#         connection.process_data_events()
#         return True
#     except pika.exceptions.AMQPError as e:
#         print("AMQP Error:", e)
#         print("...creating a new connection.")
#         return False



# # -------------------------------------------------------- END OF AMQP STUFFFFF:   -------------------------------------------------------- 




monitorBindingKey='#'



# from getAllChatIds import getAllUniqueIds
botapi = "5156607863:AAHYaukoIu6-BsYuVW2-MUp86wLUiT6HB9Y"
teleUrl = f"https://api.telegram.org/bot{botapi}/sendMessage"

def messageTele2(msg, chat_id):
    # # fetch from previous function:
    # uniqueUsers = getAllUniqueIds()

    # # error handling:
    # if teleusername not in uniqueUsers:
    #     return "User not registered in telebot"
    
    # chat_id = uniqueUsers[teleusername]
    
    payload = json.dumps({
    "chat_id": chat_id,
    "text": msg
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", teleUrl, headers=headers, data=payload)


def getSellerChatId(sellerId):
    # url = "http://localhost:9191/sellers/" + str(sellerId)

    # payload={}
    # headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)

# liqing: lliqing, 202631841
# maaruni: maars505, 202631841
    dummydata = {
    "code": 200,
    "data": {
        "sellerBankAccNo": 2147483647,
        "sellerCtcNo": 98989898,
        "sellerID": 3,
        "sellerName": "lliqing",
        "chatId": 493366384
    }
}


    return dummydata["data"]["chatId"]





def getSellerInfo(customerId):
    # current route for getting seller info:
    url = SELLERURL + "sellers"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).json()
    print(f"seller response: {response} \n")

#     dummy_data = {
#     "code": 200,
#     "data": {
#         "sellers": [
#             {
#                 "sellerBankAccNo": 774777773,
#                 "sellerCtcNo": 98989898,
#                 "sellerID": 1,
#                 "sellerName": "Cindy"
#             },
#             {
#                 "sellerBankAccNo": 983045,
#                 "sellerCtcNo": 94356788,
#                 "sellerID": 2,
#                 "sellerName": "Maarsssss"
#             }
#         ]
#     }
# }
    return response



def organiseBySeller(data):
    # data = {'code': 200, 'data': {'customerID': '1111', 'dateOfModification': 'Sat, 02 Apr 2022 10:43:46 GMT', 'dateOfPurchase': 'Sat, 02 Apr 2022 10:43:42 GMT', 'order_id': 38, 'order_item': 
    # [{'id': 120, 'itemPrice': '120.00', 'order_id': 38, 'order_item_id': 73, 'productName': 'madmmmm999', 'quantity': 1, 'sellerID': 1}, 
    # {'id': 121, 'itemPrice': '121.00', 'order_id': 38, 'order_item_id': 74, 'productName': 'madmmmm999', 'quantity': 4, 'sellerID': 2},
    # {'id': 122, 'itemPrice': '121.00', 'order_id': 38, 'order_item_id': 74, 'productName': 'madmmmm999', 'quantity': 4, 'sellerID': 2},
    # {'id': 123, 'itemPrice': '121.00', 'order_id': 38, 'order_item_id': 74, 'productName': 'madmmmm999', 'quantity': 4, 'sellerID': 2}
    # ], 
    # 'status': 'Cancelled'}}
    all_items_cancelled = data["data"]["order_item"]
    # print(f"all_items_cancelled: {all_items_cancelled}")
    uniqueSellers = {}
    for i in all_items_cancelled:
        if i["sellerID"] not in uniqueSellers:
            uniqueSellers[i["sellerID"]] = [i]

        else:
            uniqueSellers[i["sellerID"]] += [i]

    # print(f"uniqueSellers:{uniqueSellers}")
    for key, val in uniqueSellers.items():
        print(f"seller {key} ->>>>>>>> {val}")
    return uniqueSellers


def receiveOrderLog():
    amqp_setup.check_setup()
    # check_setup()
        
    queue_name = 'Activity_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

    # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    # channel.start_consuming() # an implicit loop waiting to receive messages; 

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an order log by " + __file__)

   

    bodyJson = json.loads(body)

     # ADD OWN LOGIC -- is it here?: 
    print(f"TELEBOT SENDINGGGGG body -- {bodyJson}")


    if "teleSeller" in bodyJson.keys():
        # process body to get seller id sent in message:
        uniqueSellersToText = list(set(bodyJson["teleSeller"].split("#")))
        # print(f"uniqueSellersToText: {uniqueSellersToText}")
        sellerData = organiseBySeller(bodyJson["allInfo"])
        print(f"organiseBySeller: {sellerData}")
        for seller, items in sellerData.items():
            chatId = getSellerChatId(seller)
            # print(f"chat id issss: {chatId}")
            formatedMessage4Seller = ""
            for i in items:
                currItemId = str(i["itemID"])
                currItemName = str(i["productName"])
                currItemOrderId = str(i["order_id"])
                formatedMessage4Seller += f"Item with id:{currItemId}, productName: {currItemName}, order id: {currItemOrderId} \n"

            formatedMessage4Seller += "have been cancelled!"
            print(f"this is the formated messageee: {formatedMessage4Seller}")
            messageTele2(formatedMessage4Seller, chatId)
            # print(f"seller {chatId} has been notified! with --> {items}")
    else:
        print("orderplaced no tele message sent")


    processOrderLog(json.loads(body))
    print() # print a new line feed

def processOrderLog(order):
    print("Recording an order log:")
    print(order)


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    # print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    # print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, exchangename))
    receiveOrderLog()
