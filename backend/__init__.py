# import waitress
from app import create_app

if __name__ == "__main__":
    app = create_app()
    # waitress.serve(app, host="0.0.0.0", port=42069)

    app.run(debug=True, port=42069)
