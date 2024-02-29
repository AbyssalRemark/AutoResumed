import dbtool

from json import loads as deserialize
from flask import Blueprint, Response, request
from flask_json import json_response, JsonError
from prisma.errors import UniqueViolationError
from util import is_valid_email

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
async def login() -> Response:
    """
    Takes email and password
    Returns bearer token
    """

    data = request.get_json()
    try:
        # Check JSON data has email and password fields, and that email is a valid email address
        email = data["email"]
        if not is_valid_email(email):
            raise JsonError(description=f"'{email}' is not a valid email address")
        data["password"]
    except (KeyError, TypeError, ValueError):
        raise JsonError(description="Invalid JSON value")

    token = await dbtool.login(data)

    if not token:
        raise JsonError(description="Incorrect credentials. Please try again.")
    else:
        # Return bearer token
        return json_response(token=token)


@auth.route("/logout", methods=["POST"])
async def logout() -> Response:
    """
    Invalidates the user's bearer token

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
async def register() -> Response:
    """
    Registers the user in the DB

    Takes an email and password
    Returns a confirmation of registration
    """

    data = request.get_json()
    try:
        # Check JSON data has email and password fields, and that email is a valid email address
        email = data["email"]
        if not is_valid_email(email):
            raise JsonError(description=f"'{email}' is not a valid email address")
        data["password"]
    except (KeyError, TypeError, ValueError):
        # TODO: Return more specific errors
        raise JsonError(description="Invalid JSON value")

    # Create user entry in database
    try:
        await dbtool.create_user(data)
    except UniqueViolationError:
        raise JsonError(description="Error creating user. A user with the same email already exists.")

    # Return registration confirmation
    return json_response(status="200", msg="Registration sucessful")
