import flask
from flask import request

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/create", methods=["POST"])
def create_user():
    # Check for data needed to create the user
    username = request.args.get('username', '')
    if username == '':
        return "No Username Specified", 400
    data = request.args.get('data', '')
    if data == '':
        return "No Data Specified", 400

    # Place the user into the database and return the UserID

    userid = 1

    return f"User: {userid}, Created", 201


@app.route("/get")
def get_user():

    # Check for userID in method
    userid = request.args.get('userid', '')
    if userid == '':
        return "No userid specified", 400

    # Check database

    return "User, Found", 200


@app.route("/list")
def list_users():
    return "User List", 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)
