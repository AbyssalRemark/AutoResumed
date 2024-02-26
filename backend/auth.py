from flask import Blueprint, Response, request
from flask_json import json_response

auth = Blueprint("auth", __name__)


# Takes username and password
# Returns user ID and bearer token
@auth.route("/login", methods=["POST"])
def login() -> Response:
    if request.method == "POST":
        data = request.get_json()
        print(data)

    # Check database

    # Return user ID and bearer token
    return json_response(uuid=1234, token=1234)


# Takes user ID and bearer token
@auth.route("/logout", methods=["POST"])
def logout() -> str:
    return "Sucessfully logged out"


# Takes username and password
# Returns user ID and bearer token
@auth.route("/register", methods=["POST"])
def register() -> Response:
    if request.method == "POST":
        data = request.get_json()
        print(data)

    # Create user entry in database

    # Return user ID and bearer token
    return json_response(uuid=1234, token=1234)
