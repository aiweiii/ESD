from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Daily Discover"

    #http://<hostname>:<port>/
    #http://127.0.0.1:8089/
