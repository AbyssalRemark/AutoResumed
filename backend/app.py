from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS


from auth import auth
from resume import resume

app = Flask(__name__)
json = FlaskJSON(app)
CORS(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(resume, url_prefix="/resume")
