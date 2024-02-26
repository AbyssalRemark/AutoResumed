import dbtool
import asyncio

from flask import Flask, request
from flask_json import FlaskJSON


from auth import auth

app = Flask(__name__)
json = FlaskJSON(app)
db = asyncio.run(dbtool.connect())

app.register_blueprint(auth, url_prefix="/auth")


@app.route("/resume", methods=["GET", "POST", "DELETE"])
async def resume() -> str:
    # Get JSON of resume
    if request.method == "GET":
        return "Resume"
    # Update the resume in DB
    elif request.method == "POST":
        return "Update the resume"
    # Remove the resume
    elif request.method == "DELETE":
        return "Delete the resume"
    else:
        return "Else"
