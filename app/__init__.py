from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os
from routes.estudo_routes import estudo_bp
from routes.usuario_routes import usuario_bp

jwt = JWTManager()

def create_app():
    
    load_dotenv()

    app = Flask(__name__)

    # Configurações do JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_API")
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_HEADER_TYPE"] = "Bearer"

    jwt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(estudo_bp, url_prefix="/api/estudos")
    app.register_blueprint(usuario_bp, url_prefix="/api/estudos/usuario")
    return app
