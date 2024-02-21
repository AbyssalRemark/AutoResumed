from flask import Flask, request

app = Flask(__name__)

# Bearer token is sent with every request, and check against the DB
@app.route("/login", methods=["POST", "GET"])
def login() -> str:
    print(request)
    return "Login"

@app.route("/logout")
def logout() -> str:
    return "Logout"

@app.route("/register")
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
