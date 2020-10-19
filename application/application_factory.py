from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globally accessible libraries
database = SQLAlchemy()
ma = Marshmallow()
mi = Migrate()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.DevConfig')
    app.config.from_object('config.ProdConfig')

    database.init_app(app)
    ma.init_app(app)
    mi.init_app(app, database)

    with app.app_context():
        # Include our Routes
        from application.service import routes
        from .models.item import Item

        database.create_all()  # Create sql tables for our data models

    return app
