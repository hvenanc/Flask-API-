from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from app import create_app

load_dotenv()
app = create_app()
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_API")
app.config["JWT_TOKEN_LOCATION"] = ["headers"]  # ← ESSA É A QUE ESTÁ FALTANDO
app.config["JWT_HEADER_NAME"] = "Authorization"
app.config["JWT_HEADER_TYPE"] = "Bearer"

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True)
