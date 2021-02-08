import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    )

    @app.route("/")
    def hello():
        return "Hello, World!"

    return app
