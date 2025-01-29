import os

DB_USER = "abhijeet"
DB_PASSWORD = "abhi123"
DB_NAME = "fastapi_db"
DB_HOST = "localhost"
DB_PORT = "5432"

# Get database URL from environment variable
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://flaskuser:flaskpassword@localhost:5432/flaskdb")
SQLALCHEMY_TRACK_MODIFICATIONS = False