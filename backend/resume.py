import dbtool

from cli import autoresumed
import resumed
from flask import Blueprint, request
from flask_json import JsonError, json_response

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

@resume.route("/generate", methods=["POST"])
async def generate():
    """
    Generate an HTML resume, given a token, a set of tags, and a resume template.
    """

    data = request.get_json()

    try:
       token = str(data["token"])
       tags = list(data["tags"])
       template = str(data["template"])
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>', 'tags': [ '<tag>', '<tag>', ... ], 'template': '<resume-template>' }.",
        )

    tagged_resume = dbtool.get_resume(token)
    flattened_resume = autoresumed.flatten_resume(tagged_resume, tags)
    html_resume = resumed.to_html(flattened_resume, template)

    return json_response(status="200", resume=html_resume)