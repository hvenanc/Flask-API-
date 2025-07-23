from datetime import datetime
from models.estudo import Estudo
from models.enuns import StatusEstudo
from config.firebase_config import db

class EstudoRepository:

    def __init__(self):
        self.collection = db.collection("estudos")


    def listar_todos(self, usuario_id):
        docs = self.collection.where("usuario_id", "==", usuario_id).stream()
        return [doc.to_dict() for doc in docs]
    

    def buscar_por_id(self, id, usuario_id):
        doc = self.collection.document(id).get()
        if doc.exists:
            dados = doc.to_dict()
            if dados.get("usuario_id") == usuario_id:
                return dados
        return None
    
    
    def cadastar_plano_estudo(self, disciplina, descricao, data_fim, usuario_id):
        doc = self.collection.document()
        plano_estudo = Estudo(
            id = doc.id,
            disciplina = disciplina,
            descricao = descricao,
            status= StatusEstudo.NAO_INICIADO.value,
            data_inicio = datetime.now(),
            data_fim= datetime.strptime(data_fim, "%d/%m/%Y"),
            usuario_id = usuario_id
        )
        doc.set(plano_estudo.to_json())
        return plano_estudo


    def atualizar_plano_estudo(self, id, disciplina, descricao, status, data_fim, usuario_id):
        doc_ref = self.collection.document(id)
        doc = doc_ref.get()
        if doc.exists:
            plano_estudo = doc.to_dict()
            if plano_estudo.get("usuario_id") == usuario_id:
                plano_estudo['disciplina'] = disciplina
                plano_estudo['descricao'] = descricao
                plano_estudo['status'] = StatusEstudo(status).value
                plano_estudo['data_fim'] = datetime.strptime(data_fim, "%d/%m/%Y")

                doc_ref.set(plano_estudo)
                return plano_estudo
            else:
                None

        
    def remover_plano_estudo(self, id, usuario_id):
        doc = self.collection.document(id).get()
        if doc.exists:
            dados = doc.to_dict()
            if dados.get("usuario_id") == usuario_id:
                return doc.reference.delete()
        return None