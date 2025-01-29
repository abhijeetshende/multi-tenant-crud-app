import os

DB_USER = "abhijeet"
DB_PASSWORD = "abhi123"
DB_NAME = "fastapi_db"
DB_HOST = "localhost"
DB_PORT = "5432"

# Construct the database URI dynamically
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", 
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
