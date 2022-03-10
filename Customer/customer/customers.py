from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8089/customers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class Customers(db.Model):
    __tablename__ = 'customers'
 
    custID = db.Column(db.String(13), primary_key=True)
    custName = db.Column(db.String(64), nullable=False)
    custAddress = db.Column(db.String(64), nullable=False)
    custBankAccNo = db.Column(db.Integer)
 
    def __init__(self, custID, custName, custAddress, custBankAccNo):
        self.custID = custID
        self.custName = custName
        self.custAddress = custAddress
        self.custBankAccNo = custBankAccNo
 
    def json(self):
        return {"custID": self.custID, "custName": self.custName, "custAddress": self.custAddress, "custBankAccNo": self.custBankAccNo}

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
def create_book(custID):
 
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
            "code": 201,
            "data": customer.json()
        } 
    ), 201

 
if __name__ == '__main__':
    app.run(port=5001, debug=True)
