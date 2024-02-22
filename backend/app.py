from flask import Flask, request
from flask_json import FlaskJSON

app = Flask(__name__)
json = FlaskJSON(app)

# User ID and bearer token are sent with every request, and checked against the DB

# Takes username and password
# Returns user ID and bearer token
@app.route("/login", methods=["POST"])
def login() -> str:
    if request.method == "POST":
        data = request.get_json()
        print(data)

    return "Login"

# Takes user ID and bearer token
@app.route("/logout", methods=["POST"])
def logout() -> str:
    return "Sucessfully logged out"

# Takes username and password
# Returns user ID and bearer token
@app.route("/register", methods=["POST"])
def register() -> str:
    return "Register"

@app.route("/resume", methods=["GET", "POST", "DELETE"])
def resume() -> str:
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
