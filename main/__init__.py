import os

from flask import (Flask, render_template)

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route("/gaming/safety/player_safety_checklist.html")
    def player_safety():
        return render_template("gaming/safety/player_safety_checklist.html.j2")

    return app
