#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import json
import os

import amqp_setup
from flask import Flask, request, jsonify
import requests
# telegram imports:
from sendTeleUpdate import messageTele



monitorBindingKey='#'



# from getAllChatIds import getAllUniqueIds
url = "https://api.telegram.org/bot5181590371:AAFQdlbl9jcYzStA0zGe9I_s6bM_77p5Gic/sendMessage"

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

    response = requests.request("GET", url, headers=headers, data=payload)


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
    url = "http://localhost:9191/sellers"
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
        
    queue_name = 'Activity_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an order log by " + __file__)

   

    bodyJson = json.loads(body)

     # ADD OWN LOGIC -- is it here?: 
    # print(f"TELEBOT SENDINGGGGG body -- {bodyJson}")


    if "teleSeller" in bodyJson.keys():
        # process body to get seller id sent in message:
        uniqueSellersToText = list(set(bodyJson["teleSeller"].split("#")))
        # print(f"uniqueSellersToText: {uniqueSellersToText}")
        sellerData = organiseBySeller(bodyJson["allInfo"])
        
        for seller, items in sellerData.items():
            chatId = getSellerChatId(seller)
            # print(f"chat id issss: {chatId}")
            formatedMessage4Seller = ""
            for i in items:
                currItemId = i["id"]
                currItemName = i["productName"]
                currItemOrderId = i["order_id"]
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
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveOrderLog()
