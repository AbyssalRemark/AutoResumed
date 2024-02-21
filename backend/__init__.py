from flask import Flask

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return "<p>Hello, world<p>"
