from distutils.log import debug
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String )

#------------------ login ------------------------#

app.secret_key = "esdproject"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "324188183280-imf2vhl08f35oh4p7hdd0900k9st7si0.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:3000/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return render_template("error.html")  # Authorization required
        else:
            return function()

    return wrapper

#------------------ routing ------------------------#

@app.route("/")
def home():
    if "google_id" in session: 
        user = session["name"]
    else: 
        user = ""
    return render_template("home.html", user=user)


@app.route("/productDetails/<itemId>")
def pDesc(itemId):
    return render_template('productDetails.html')


@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/orderhistory") #homepage or whatever that needs to have the user login then can see
@login_is_required
def protected_area():
    return render_template("orderhistory.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="localhost", port=3000, debug=True)


    # http://<hostname>:<port>/
    # http://127.0.0.1:8089/
