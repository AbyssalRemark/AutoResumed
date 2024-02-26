import dbtool
import app

from flask import Blueprint, Response, request
from flask_json import json_response

auth = Blueprint("auth", __name__)


# Takes username and password
# Returns user ID and bearer token
@auth.route("/login", methods=["POST"])
async def login() -> Response:
    if request.method == "POST":
        data = request.get_json()
        print(data)

    # Check database

    # Return user ID and bearer token
    return json_response(uuid=1234, token=1234)


# Takes user ID and bearer token
@auth.route("/logout", methods=["POST"])
async def logout() -> str:
    return "Sucessfully logged out"


# Takes username and password
# Returns user ID and bearer token
@auth.route("/register", methods=["POST"])
async def register() -> Response:
    if request.method == "POST":
        data = request.get_json()

        # Create user entry in database
        await dbtool.create_user(app.db, data)

        # Return user ID and bearer token
        return json_response(uuid=1234, token=1234)
    else:
        return json_response(status="401", msg="Bad JSON >:(")

