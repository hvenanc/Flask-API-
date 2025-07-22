from models.estudo import Estudo
from models.enuns import StatusEstudo
from datetime import datetime

class EstudoRepository:

    def __init__(self):
        self.planos_estudo = []

    
    def listar_todos(self):
        return self.planos_estudo
    

    def buscar_por_id(self, id: str):
        return next((estudo for estudo in self.planos_estudo if estudo.id == id), None)
    
    
    def cadastar_plano_estudo(self, disciplina, descricao, data_fim):
        plano_estudo = Estudo(
            disciplina = disciplina,
            descricao = descricao,
            status= StatusEstudo.NAO_INICIADO.value,
            data_inicio = datetime.now(), #Possível erro
            data_fim= datetime.strptime(data_fim, "%d/%m/%Y").date()
        )
        self.planos_estudo.append(plano_estudo)
        return plano_estudo
    
    
    def atualizar_plano_estudo(self, id, disciplina, descricao, status, data_fim):
        plano_estudo = self.buscar_por_id(id)
        if plano_estudo:
            plano_estudo.disciplina = disciplina
            plano_estudo.descricao = descricao
            plano_estudo.status = StatusEstudo(status)
            plano_estudo.data_fim = datetime.strptime(data_fim, "%d/%m/%Y").date()

        return plano_estudo

        
    def remover_plano_estudo(self, id):
        plano_estudo = self.buscar_por_id(id)
        if plano_estudo:
            self.planos_estudo.remove(plano_estudo)

        return plano_estudo
