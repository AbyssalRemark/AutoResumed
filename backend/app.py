from flask import Flask, Response, request
from flask_json import FlaskJSON, JsonError
from flask_cors import CORS


from auth import auth
from resume import resume

import dbtool

app = Flask(__name__)
json = FlaskJSON(app)
CORS(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(resume, url_prefix="/resume")
