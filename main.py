import flask
from flask import request

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user", methods=["POST"])
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


@app.route("/user", methods=["GET"])
def get_user():

    # Check for userID in method
    userid = request.args.get('userid', '')
    if userid == '':
        return "No userid specified", 400

    # Check database
    user = get_user_from_db()
    if user == '':
        return f"User not found with ID: {userid}", 404

    return "User, Found", 200


@app.route("/users")
def list_users():

    # List all users from the database :)
    users = get_all_users_from_db()
    return [user.to_json() for user in users], 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)
