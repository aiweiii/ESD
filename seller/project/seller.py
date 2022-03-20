from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
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


# @app.route("/book/<string:isbn13>", methods=['PUT'])
# def update_book(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         data = request.get_json()
#         if data['title']:
#             book.title = data['title']
#         if data['price']:
#             book.price = data['price']
#         if data['availability']:
#             book.availability = data['availability'] 
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": book.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "isbn13": isbn13
#             },
#             "message": "Book not found."
#         }
#     ), 404


# @app.route("/book/<string:isbn13>", methods=['DELETE'])
# def delete_book(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         db.session.delete(book)
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "isbn13": isbn13
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "isbn13": isbn13
#             },
#             "message": "Book not found."
#         }
#     ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
