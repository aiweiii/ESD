from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = [
    {
    "Id" : 1,
    "Name" : "Ong Hong Seng",
    "Gender" : "Male"
    },
    {
    "Id" : 2,
    "Name" : "Mr Bean",
    "Gender" : "Male"
    }
]

@app.route('/student')
def get_all_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)
