from flask import Flask, request
from flask_json import FlaskJSON, JsonError


from auth import auth

# import dbtool

app = Flask(__name__)
json = FlaskJSON(app)

app.register_blueprint(auth, url_prefix="/auth")


@app.route("/resume", methods=["GET", "POST", "DELETE"])
async def resume() -> str:
    data = request.get_json()
    try:
        token = str(data["token"])
        # TODO: Derive userID from bearer token

    except (KeyError, TypeError, ValueError):
        raise JsonError(description="Invalid JSON value")

    # Get JSON of resume
    if request.method == "GET":
        # resume = await dbtool.get_resume(user_id)
        return "Resume"
    # Update the resume in DB
    elif request.method == "POST":
        return "Update the resume"
    # Remove the resume
    elif request.method == "DELETE":
        return "Delete the resume"
    else:
        return "Else"
