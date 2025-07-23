from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from service.usuario_service import UsuarioService

usuario_bp = Blueprint("usuarios", __name__)
service = UsuarioService()


@usuario_bp.route("/registro", methods=["POST"])
def registro():
    dados = request.json
    usuario = service.criar_usuario(dados)
    return jsonify(usuario), 201


@usuario_bp.route("/login", methods = ["POST"])
def login():
    dados = request.json
    usuario = service.autenticar(dados)
    if not usuario:
        return jsonify({"erro: Credenciais inválidas"}), 401
    
    token = create_access_token(identity = usuario["id"])
    return jsonify({"token": token}), 200