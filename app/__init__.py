from flask import Flask
from routes.estudo_routes import estudo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(estudo_bp, url_prefix="/api/estudos")
    return app
