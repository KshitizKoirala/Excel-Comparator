import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from .config.config import Config

from .extensions import db

# custom routes
from .users.routes import users
from .excel_comparator.routes import excel

# Loading the .env files
load_dotenv(find_dotenv())


# Create app to initailize the database for the running applications
def create_app(config_class=Config):
    app = Flask(__name__)
    # Loading the configuration file
    app.config.from_object(Config)

    # initiatializing the database here to remove circular dependencies
    db.init_app(app)
    # registering blueprints for routes to make our application modular
    app.register_blueprint(excel)
    app.register_blueprint(users)
    return app
