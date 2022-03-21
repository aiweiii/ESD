from email import message
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
 
class Customers(db.Model):
    __tablename__ = 'customers'
 
    custID = db.Column(db.String(13), primary_key=True)
    custName = db.Column(db.String(64), nullable=False)
    custAddress = db.Column(db.String(64), nullable=False)
    custCCNo = db.Column(db.Integer)
 
    def __init__(self, custID, custName, custAddress, custCCNo):
        self.custID = custID
        self.custName = custName
        self.custAddress = custAddress
        self.custCCNo = custCCNo
 
    def json(self):
        return {"custID": self.custID, "custName": self.custName, "custAddress": self.custAddress, "custCCNo": self.custCCNo}

#get all
@app.route("/customers")
def get_all():
    custList = Customers.query.all()
    if len(custList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "customers": [customer.json() for customer in custList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404

#get customer by ID
@app.route("/customers/<string:custID>")
def find_by_custID(custID):
    customer = Customers.query.filter_by(custID=custID).first()
    if customer:
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404


#create customer
@app.route("/customers/<string:custID>", methods=['POST'])
def create_cust(custID):
 
    if (Customers.query.filter_by(custID=custID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "custID": custID
                },
                "message": "Customer already exists."
            }
        ), 400
 
    data = request.get_json()
    customer = Customers(custID, **data)
 
    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "custID": custID
                },
                "message": "An error occurred creating the customer."
            }
        ), 500
 
    return jsonify(
        {
            "code": 200,
            "data": customer.json()
        } 
    ), 201

# update customer info
@app.route("/customers/<string:custID>", methods=['PUT'])
def update_cust(custID):
    try:
        cust = Customers.query.filter_by(custID=custID).first()
        if not cust: 
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "custID": custID
                    },
                    "message": "Customer not found."
                }
            ), 404

        #update
        data = request.get_json()
        if data['custName']:
            cust.custName = data['custName']
        if data['custAddress']:
            cust.custAddress = data['custAddress']
        if data['custCCNo']:
            cust.custCCNo = data['custCCNo']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": cust.json(), 
                "message": "Successfully updated customer information"
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "custID": custID
                },
                "message": "An error occurred while updating customer's information. " + str(e)
            }
        ), 500
    


# delete customer
@app.route("/customers/<string:custID>", methods=['DELETE'])
def delete_cust(custID):
    cust = Customers.query.filter_by(custID=custID).first()
    if cust:
        db.session.delete(cust)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "custID": custID
                },
                "message": "Customer successfully deleted."
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "custID": custID
            },
            "message": "Customer not found."
        }
    ), 404
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)