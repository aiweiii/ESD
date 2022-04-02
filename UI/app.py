from distutils.log import debug
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String )


@app.route("/")
def home():
    return render_template('homepage.html')


@app.route("/productDetails/<itemId>")
def pDesc(itemId):
    return render_template('productDetails.html')


@app.route("/cart")
def cart():
    return render_template('cart.html')


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="localhost", port=3000, debug=True)


    # http://<hostname>:<port>/
    # http://127.0.0.1:8089/
