from distutils.log import debug
from flask import Flask, render_template, url_for
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# CORS(app)
# api_v1_cors_config = {
#     "origins": ["http://localhost:5000"],
#     "methods": ["OPTIONS", "GET", "POST"],
#     "allow_headers": ["Authorization"]
# }
# CORS(app, resources={"/api/v1/*": api_v1_cors_config})


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String )


@app.route("/")
def index():
    return render_template('homepage.html')


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="localhost", port=3000, debug=True)


    # http://<hostname>:<port>/
    # http://127.0.0.1:8089/
