from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.secret_key = "Hello World"

    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    return app