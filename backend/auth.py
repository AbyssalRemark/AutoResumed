import dbtool

from flask import Blueprint, Response, request
from flask_json import json_response, JsonError
from prisma.errors import UniqueViolationError

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
async def login() -> Response:
    """
    Takes email and password
    Returns bearer token
    """

    data = request.get_json()
    try:
        # Pull email and password out of JSON data
        email = str(data.get("email"))
        password = str(data.get("password"))
    except (KeyError, TypeError, ValueError):
        raise JsonError(description="Invalid JSON value")

    # TODO: Check database

    # Return bearer token
    return json_response(token=1234)


@auth.route("/logout", methods=["POST"])
async def logout():
    """
    Takes a bearer token
    Returns a confirmation of logout
    """

    data = request.get_json()
    try:
        token = str(data.get("token"))
    except (KeyError, TypeError, ValueError):
        raise JsonError(description="Invalid JSON value")

    # TODO: Invalidate the bearer token in the DB

    return json_response(status=200, msg="Loguout sucessful")


@auth.route("/register", methods=["POST"])
async def register():
    """
    Takes a username and password
    Returns a confirmation of registration
    """

    data = request.get_json()
    try:
        # Pull email and password out of JSON data
        email = str(data.get("email"))
        password = str(data.get("password"))

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
