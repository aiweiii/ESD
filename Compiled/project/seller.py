from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
# new cors error edit:
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/seller'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#db.Column(db.Float(precision=2), nullable=False)
class Seller(db.Model):
    __tablename__ = 'seller'

    sellerID = db.Column(db.String(13), primary_key=True)
    sellerName = db.Column(db.String(64), nullable=False)
    sellerCtcNo =  db.Column(db.Integer, nullable=False)
    sellerBankAccNo = db.Column(db.Integer, nullable=False)

    def __init__(self, sellerID, sellerName, sellerCtcNo, sellerBankAccNo):
        self.sellerID = sellerID
        self.sellerName = sellerName
        self.sellerCtcNo = sellerCtcNo
        self.sellerBankAccNo = sellerBankAccNo

    def json(self):
        return {"sellerID": self.sellerID, "sellerName": self.sellerName, "sellerCtcNo": self.sellerCtcNo, "sellerBankAccNo": self.sellerBankAccNo}

#get seller details
@app.route("/sellers")
def get_all():
    sellerList = Seller.query.all()
    if len(sellerList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "sellers": [seller.json() for seller in sellerList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no sellers."
        }
    ), 404

#get seller ID
@app.route("/sellers/<string:sellerID>")
def find_by_sellerID(sellerID):
    seller = Seller.query.filter_by(sellerID=sellerID).first()
    if seller:
        return jsonify(
            {
                "code": 200,
                "data": seller.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Seller does not exist."
        }
    ), 404


#create seller
@app.route("/sellers/<string:sellerID>", methods=['POST'])
def create_seller(sellerID):
 
    if (Seller.query.filter_by(sellerID=sellerID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "sellerID": sellerID
                },
                "message": "Seller already exists."
            }
        ), 400
 
    data = request.get_json()
    seller = Seller(sellerID, **data)
 
    try:
        db.session.add(seller)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "sellerID": sellerID
                },
                "message": "An error occurred creating the customer."
            }
        ), 500
 
    return jsonify(
        {
            "code": 200,
            "data": seller.json()
        } 
    ), 201

# update customer info
@app.route("/sellers/<string:sellerID>", methods=['PUT'])
def update_seller(sellerID):
    try:
        seller = Seller.query.filter_by(sellerID=sellerID).first()
        if not seller: 
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "sellerID": sellerID
                    },
                    "message": "Seller not found."
                }
            ), 404

        #update
        data = request.get_json()
        if data['sellerName']:
            seller.sellerName = data['sellerName']
        if data['sellerCtcNo']:
            seller.sellerCtcNo = data['sellerCtcNo']
        if data['sellerBankAccNo']:
            seller.sellerBankAccNo = data['sellerBankAccNo']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": seller.json(), 
                "message": "Successfully updated customer information"
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "sellerID": sellerID
                },
                "message": "An error occurred while updating customer's information. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)
