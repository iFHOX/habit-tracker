from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(TestConfig):
    app = Flask(__name__)
    app.config.from_object(TestConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints are going to be here

    return app