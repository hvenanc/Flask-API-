from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from app import create_app

load_dotenv()
app = create_app()
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_API")

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True, port=0000)
