from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.estudo_service import EstudoService

estudo_bp = Blueprint("estudos", __name__)
service = EstudoService()

@estudo_bp.route("/", methods=["GET"])
@jwt_required()
def listar_todos():
    usuario_id = get_jwt_identity()
    return jsonify(service.listar_planos_estudo(usuario_id))


@estudo_bp.route("/<string:id>", methods=["GET"])
@jwt_required()
def listar_por_id(id):
    usuario_id = get_jwt_identity()
    plano_estudo = service.buscar_plano_estudo(id, usuario_id)
    if plano_estudo:
        return jsonify(plano_estudo), 200
    return jsonify({"erro": "Plano de estudo não encontrado"}), 404


@estudo_bp.route("/", methods=["POST"])
@jwt_required()
def criar():
    usuario_id = get_jwt_identity()
    dados = request.json
    plano_estudo = service.criar_plano_estudo(dados, usuario_id)
    return jsonify(plano_estudo), 201


@estudo_bp.route("/editar/<string:id>", methods=["PUT"])
@jwt_required()
def editar(id):
    usuario_id = get_jwt_identity()
    print(usuario_id)
    dados = request.json
    plano_estudo = service.atualizar_plano_estudo(id, dados, usuario_id)
    if plano_estudo:
        return jsonify(plano_estudo), 200
    return jsonify({"erro": "Plano de estudo não encontrado"}), 404


@estudo_bp.route("/deletar/<string:id>", methods=["DELETE"])
@jwt_required()
def deletar(id):
    usuario_id = get_jwt_identity()
    plano_estudo = service.deletar_plano_estudo(id, usuario_id)
    if plano_estudo:
        return ' ', 204
    else:
        return jsonify({"erro": "Plano de estudo não encontrado"}), 404