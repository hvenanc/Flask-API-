from flask import Blueprint, request, jsonify
from service.estudo_service import EstudoService

estudo_bp = Blueprint("estudos", __name__)
service = EstudoService()

@estudo_bp.route("/", methods=["GET"])
def listar_todos():
    return jsonify(service.listar_planos_estudo())


@estudo_bp.route("/<string:id>", methods=["GET"])
def listar_por_id(id):
    plano_estudo = service.buscar_plano_estudo(id)
    if plano_estudo:
        return jsonify(plano_estudo), 200
    return jsonify({"erro": "Plano de estudo não encontrado"}), 404


@estudo_bp.route("/", methods=["POST"])
def criar():
    dados = request.json
    plano_estudo = service.criar_plano_estudo(dados)
    return jsonify(plano_estudo), 201


@estudo_bp.route("/editar/<string:id>", methods=["PUT"])
def editar(id):
    dados = request.json
    plano_estudo = service.atualizar_plano_estudo(id, dados)
    if plano_estudo:
        return jsonify(plano_estudo), 200
    return jsonify({"erro": "Plano de estudo não encontrado"}), 404


@estudo_bp.route("/deletar/<string:id>", methods=["DELETE"])
def deletar(id):
    plano_estudo = service.deletar_plano_estudo(id)
    if plano_estudo:
        return ' ', 204
    else:
        return jsonify({"erro": "Plano de estudo não encontrado"}), 404