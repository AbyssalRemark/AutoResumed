import dbtool
import subprocess
import os

from cli import autoresumed, resumed
from cli.resumed import InvalidTemplate
from flask import Blueprint, Response, request, jsonify, send_file
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

    if await dbtool.is_authorized(token) == False:
        raise JsonError(
            401,
            error="unauthorized",
            message="Token unauthorized.",
            detail="The given token is not authorized. Try again with a different token."
        )

    resume_dict = await dbtool.get_resume_clean(token)
    resume = jsonify(resume_dict)
    return resume


@resume.route("/update", methods=["PUT"])
async def update():
    data = request.get_json()

    try:
        token = str(data["token"])
        resume = data["resume"]
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>', 'resume': '<resume>' }.",
        )

    if await dbtool.is_authorized(token) == False:
        raise JsonError(
            401,
            error="unauthorized",
            message="Token unauthorized.",
            detail="The given token is not authorized. Try again with a different token."
        )

    resume_in_db = await dbtool.update_resume(resume, token)

    return json_response(status='200', resume=resume_in_db)


@resume.route("/generate", methods=["POST"])
async def generate():
    """
    Generate an HTML resume, given a token, a set of tags, a resume template, and whether to output HTML or PDF.
    """

    data = request.get_json()

    try:
       token = str(data["token"])
       tags = list(data["tags"])
       template = str(data["template"])
       type = str(data["type"])
    except (KeyError, TypeError, ValueError):
        raise JsonError(
            400,
            error="invalid-json",
            message="Invalid JSON data.",
            detail="We expect { 'token': '<bearer-token>', 'tags': [ '<tag>', '<tag>', ... ], 'template': '<resume-template>', 'type': '<html or pdf>' }.",
        )

    if await dbtool.is_authorized(token) == False:
        raise JsonError(
            401,
            error="unauthorized",
            message="Token unauthorized.",
            detail="The given token is not authorized. Try again with a different token."
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

    if type == "html":
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
    elif type == "pdf":
        try:
            resumed.to_html(flattened_resume, template, True)
        except InvalidTemplate:
            raise JsonError(
                400,
                error="invalid-template",
                message=f"Invalid template: {template}.",
                detail="Make sure the given template exists."
            )

        cwd = os.getcwd()
        html_file_path = os.path.join(cwd, "resume.html")
        output_file_path = os.path.join(cwd, "resume.pdf")

        subprocess.run(["html2pdf", html_file_path, "-o", output_file_path])

        return send_file(output_file_path)
    else:
        raise JsonError(
            400,
            error="invalid-type",
            message="The given type is invalid.",
            detail="Try giving either 'html' or 'pdf'."
        )

@resume.route("/tags", methods=["POST"])
async def tags():
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

    if await dbtool.is_authorized(token) == False:
        raise JsonError(
            401,
            error="unauthorized",
            message="Token unauthorized.",
            detail="The given token is not authorized. Try again with a different token."
        )

    tags = await dbtool.get_tags(token)

    return json_response(status="200", tags=tags)
