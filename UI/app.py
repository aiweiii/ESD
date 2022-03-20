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
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


    # http://<hostname>:<port>/
    # http://127.0.0.1:8089/
