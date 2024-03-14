from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS


from auth import auth
from resume import resume


def create_app() -> Flask:
    app = Flask(__name__)

    FlaskJSON(app)
    CORS(app)

    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(resume, url_prefix="/api/resume")

    return app
