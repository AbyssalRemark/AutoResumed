import dbtool

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

    # Check that JSON data has email and password fields
    try:
        email = data["email"]
        data["password"]
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'email': '<email>', 'password': '<password>' }.",
        )

    # Validate email address
    if not is_valid_email(email):
        raise JsonError(
            400,
            error="invalid-email-address",
            message=f"'{email}' is not a valid email address.",
            detail="Try an email address in this form: me@example.com.",
        )

    try:
        token = await dbtool.login(data)
    # An AttributeError is raised if the user doesn't exist, because Prisma returns None
    except AttributeError:
        raise JsonError(
            401,
            error="nonexistent-user",
            message="A username with the given email and password doesn't exist",
            detail="Please retry with a different email address, or register a user.",
        )

    if not token:
        raise JsonError(
            401,
            error="incorrect-credentials",
            message="The given credentials are incorrect.",
            detail="Please retry with different credentials.",
        )
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

    # Check that the JSON data has a token field
    try:
        data["token"]
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>' }.",
        )

    # TODO: Invalidate the bearer token in the DB

    return json_response(message="Logout sucessful.")


@auth.route("/register", methods=["POST"])
async def register() -> Response:
    """
    Registers the user in the DB

    Takes an email and password
    Returns a confirmation of registration
    """

    data = request.get_json()

    # Check that JSON data has email and password fields
    try:
        email = data["email"]
        data["password"]
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data",
            detail="We expect { 'email': '<email>', 'password': '<password>' }.",
        )

    # Validate email address
    if not is_valid_email(email):
        raise JsonError(
            400,
            error="invalid-email-address",
            message=f"'{email}' is not a valid email address.",
            detail="Try an email address in this form: me@example.com.",
        )

    # Create user entry in database
    try:
        await dbtool.create_user(data)
    except UniqueViolationError:
        raise JsonError(
            409,
            error="user-exists",
            message="Error creating user.",
            detail="A user with the same email already exists.",
        )

    # Return registration confirmation
    return json_response(message="Registration successful.")
