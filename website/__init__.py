from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path

#creating db object
db = SQLAlchemy()
DB_NAME = "tasks.db"

def create_app():
    ''' Function responsible for creating the web app and define the env variables '''

    # creating flask app
    app = Flask(__name__)

    # defining environment config | Development
    app.config['SECRET_KEY'] = "hello world"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initiating DB in app
    db.init_app(app)

    from .models import Task

    #creates DB file
    create_database(app)

    #adding blueprint routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    return app

def create_database(app):
    ''' Function responsible for creating db file if doesnt exist '''

    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
