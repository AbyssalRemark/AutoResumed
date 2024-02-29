import dbtool

from flask import Blueprint, Response, request
from flask_json import json_response, JsonError
from prisma.errors import UniqueViolationError

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


# Takes a bearer token
@auth.route("/logout", methods=["POST"])
async def logout() -> str:
    # TODO: Invalidate the bearer token in the DB
    return "Sucessfully logged out"


# Takes username and password
# Returns a confirmation of registration
@auth.route("/register", methods=["POST"])
async def register():
    data = request.get_json()
    try:
        # Pull email and password out of JSON data
        email = str(data["email"])
        password = str(data["password"])

        user = { "email": email, "password": password }
    except (KeyError, TypeError, ValueError):
        raise JsonError(description="Invalid JSON value")

    # Create user entry in database
    try:
        await dbtool.create_user(user)
    except UniqueViolationError:
        raise JsonError(description="Error creating user. A user with the same email already exists.")

    # Return registration confirmation
    return json_response(status="200", msg="Registration sucessful")
