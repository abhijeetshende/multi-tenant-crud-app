from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # ✅ Ensure this is the only instance used across the app
