from app import create_app
from app.database import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():  # ✅ Ensure the app context is created
        db.create_all()  # ✅ Create tables if they don't exist
    app.run(host="0.0.0.0", port=5000, debug=True)

