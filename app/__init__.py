from flask import Flask
from routes.estudo_routes import estudo_bp
from routes.usuario_routes import usuario_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(estudo_bp, url_prefix="/api/estudos")
    app.register_blueprint(usuario_bp, url_prefix="/api/estudos/usuario")
    return app
