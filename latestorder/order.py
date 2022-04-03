#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

# import os
# from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# import os, sys
from datetime import datetime
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3308/order'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/seller'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    dateOfPurchase = db.Column(db.DateTime, nullable=False, default=datetime.now)
    dateOfModification = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def json(self):
        dto = {
            'order_id': self.order_id,
            'customerID': self.customerID,
            'status': self.status,
            'dateOfPurchase': self.dateOfPurchase,
            'dateOfModification': self.dateOfModification
        }

        dto['order_item'] = []
        for oi in self.order_item:
            dto['order_item'].append(oi.json())

        return dto


class Order_Item(db.Model):
    __tablename__ = 'order_item'

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey(
        'order.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    sellerID = db.Column(db.Integer, nullable=False)
    itemID = db.Column(db.Integer, nullable=False)
    productName = db.Column(db.String(13), nullable=False)
    itemPrice = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    order = db.relationship(
        'Order', primaryjoin='Order_Item.order_id == Order.order_id', backref='order_item')
    def json(self):
        return {'order_item_id': self.order_item_id,  'order_id': self.order_id, 'sellerID': self.sellerID, 'itemID': self.itemID,
        'productName': self.productName, 'itemPrice': self.itemPrice, 'quantity': self.quantity}


@app.route("/order")
def get_all():

    print("going into 5001 order route")
    orderlist = Order.query.all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404


@app.route("/order/<string:order_id>")
def find_by_order_id(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "order_id": order_id
            },
            "message": "Order not found."
        }
    ), 404


@app.route("/order", methods=['POST'])
def create_order():
    newrequest = json.loads(request.json)
    customer_id = newrequest["customer_id"]
    order = Order(customerID=customer_id, status='PaymentCompleted')
    cart_item =  newrequest["cart_item"]
    num = 3
    for item in cart_item:
        order.order_item.append(Order_Item(
            sellerID=item['sellerId'], itemID=item['itemId'],
            productName=item['itemName'], itemPrice=item['itemPrice'],
            quantity=item['itemQuantity']
            ))
        num += 1

    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500
    
    print(json.dumps(order.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": order.json()["order_id"]
        }
    ), 201


@app.route("/order/<string:order_id>", methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.filter_by(order_id=order_id).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": order_id
                    },
                    "message": "Order not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['status']:
            order.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": order.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": order_id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
