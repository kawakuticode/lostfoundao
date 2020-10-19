from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
database = SQLAlchemy()
ma = Marshmallow()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    database.init_app(app)
    ma.init_app(app)

    with app.app_context():
        # Include our Routes
        database.create_all()  # Create sql tables for our data models

    return app
