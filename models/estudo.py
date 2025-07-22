import uuid
from models.enuns import StatusEstudo

class Estudo:
    def __init__(self, disciplina: str, descricao: str, status: StatusEstudo, data_inicio, data_fim,id: str = None):
        self.id = id or str(uuid.uuid4())
        self.disciplina = disciplina
        self.descricao = descricao
        # Garante que o status seja sempre uma instância do Enum
        if isinstance(status, StatusEstudo):
            self.status = status
        else:
            self.status = StatusEstudo(status)
        
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def to_json(self):
        """
        Retorna uma representação em dicionário do objeto Estudo.
        """
        return {
            "id": str(self.id),
            "disciplina": self.disciplina,
            "descricao": self.descricao,
            "status": self.status.value,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }

    


