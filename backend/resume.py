from flask import Blueprint, request
from flask_json import JsonError

resume = Blueprint("resume", __name__)

@resume.route("/get", methods=["POST"])
async def get():
    data = request.get_json()

    try:
        token = str(data["token"])
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>' }.",
        )

    return "Resume"

@resume.route("/update", methods=["PUT"])
async def update():
    data = request.get_json()

    try:
        token = str(data["token"])
        resume = str(data["resume"])
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>', 'resume': '<resume>' }.",
        )

    return "Fine"
