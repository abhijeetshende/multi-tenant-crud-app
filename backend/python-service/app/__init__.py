from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI

# Create a single SQLAlchemy instance
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with the app
    db.init_app(app)  # ✅ Important: This must be called

    migrate.init_app(app, db)

    # Register Blueprints
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
