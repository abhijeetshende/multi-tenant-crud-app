from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI
from app.database import db  # ✅ Import the db instance
from flasgger import Swagger  # ✅ Import Flasgger


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with the app
    db.init_app(app)  # ✅ Initialize db properly
    migrate.init_app(app, db)
    Swagger(app)

    # Register Blueprints within app context
    with app.app_context():
        from app.routes.items import api_blueprint
        from app.routes.todos import todo_blueprint  # ✅ Import new todo blueprint

        app.register_blueprint(api_blueprint)
        app.register_blueprint(todo_blueprint)

    return app
