from repository.estudo_repository import EstudoRepository

class EstudoService:

    def __init__(self):
        self.estudo_repository = EstudoRepository()


    def listar_planos_estudo(self):
        return [estudo.to_json() for estudo in self.estudo_repository.listar_todos()]
    

    def buscar_plano_estudo(self, id):
        plano_estudo = self.estudo_repository.buscar_por_id(id)
        return plano_estudo.to_json() if plano_estudo else None
    

    def criar_plano_estudo(self, dados):
        plano_estudo = self.estudo_repository.cadastar_plano_estudo(
            disciplina = dados['disciplina'],
            descricao = dados['descricao'],
            data_fim= dados['data_fim']
        )
        return plano_estudo.to_json()
    

    def atualizar_plano_estudo(self, id, dados):
        plano_estudo = self.estudo_repository.atualizar_plano_estudo(
            id = id,
            disciplina = dados['disciplina'],
            descricao = dados['descricao'],
            status = dados['status'],
            data_fim= dados['data_fim']
        )
        return plano_estudo.to_json() if plano_estudo else None
    

    def deletar_plano_estudo(self, id):
        plano_estudo = self.estudo_repository.remover_plano_estudo(id)
        return plano_estudo.to_json() if plano_estudo else None