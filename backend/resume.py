import dbtool

from cli import autoresumed, resumed
from cli.resumed import InvalidTemplate
from flask import Blueprint, request, jsonify
from flask_json import JsonError, json_response

resume = Blueprint("resume", __name__)

@resume.route("/get", methods=["POST"])
async def get():
    data = request.get_json()

    try:
        token = str(data["token"])
        resume_dict = await dbtool.get_resume_clean(token)
        resume = jsonify(resume_dict)

    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>' }.",
        )

    return resume

@resume.route("/update", methods=["PUT"])
async def update():
    data = request.get_json()

    try:
        token = str(data["token"])
        resume = data["resume"]
        resume_in_db =await dbtool.update_resume(resume, token)
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>', 'resume': '<resume>' }.",
        )

    return json_response(status='200', resume=resume_in_db)

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

    if len(tags) == 0:
        raise JsonError(
            400,
            error="missing-tags",
            message="Missing tags.",
            detail="Tags are required for generating a resume."
        )
    if len(template) == 0:
        raise JsonError(
            400,
            error="missing-template",
            message="Missing template.",
            detail="A template is required for generating a resume."
        )

    try:
        tagged_resume = await dbtool.get_resume_clean(token)
    except IndexError:
        raise JsonError(
            404,
            error="no-basics-content",
            message="No content in `basics` field.",
            detail="No basic content has been defined in the `basics` field."
        )

    try:
        flattened_resume = autoresumed.flatten_resume(tagged_resume, tags)
    except TypeError:
        raise JsonError(
            404,
            error="no-tag-match",
            message=f"No match for tags: {tags}.",
            detail="Make sure the given tags exist in the resume."
        )

    try:
        html_resume = resumed.to_html(flattened_resume, template)
    except InvalidTemplate:
        raise JsonError(
            400,
            error="invalid-template",
            message=f"Invalid template: {template}.",
            detail="Make sure the given template exists."
        )

    return json_response(status="200", resume=html_resume)
