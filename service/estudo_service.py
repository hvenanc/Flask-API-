from repository.estudo_repositoryfb import EstudoRepository

class EstudoService:

    def __init__(self):
        self.estudo_repository = EstudoRepository()


    def listar_planos_estudo(self, usuario_id):
        return self.estudo_repository.listar_todos(usuario_id)
    

    def buscar_plano_estudo(self, id, usuario_id):
        return self.estudo_repository.buscar_por_id(id, usuario_id)
    

    def criar_plano_estudo(self, dados, usuario_id):
        plano_estudo = self.estudo_repository.cadastar_plano_estudo(
            disciplina = dados['disciplina'],
            descricao = dados['descricao'],
            data_fim= dados['data_fim'],
            usuario_id = usuario_id
        )
        return plano_estudo.to_json()
    

    def atualizar_plano_estudo(self, id, dados, usuario_id):
        plano_estudo = self.estudo_repository.atualizar_plano_estudo(
            id = id,
            disciplina = dados['disciplina'],
            descricao = dados['descricao'],
            status = dados['status'],
            data_fim= dados['data_fim'],
            usuario_id = usuario_id
        )
        return plano_estudo
    

    def deletar_plano_estudo(self, id, usuario_id):
        return self.estudo_repository.remover_plano_estudo(id, usuario_id)
        