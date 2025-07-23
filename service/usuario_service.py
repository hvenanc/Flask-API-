from repository.usuario_repository import UsuarioRepositoty


class UsuarioService:

    def __init__(self):
        self.usuario_repository = UsuarioRepositoty()


    def criar_usuario(self, dados):
        usuario = self.usuario_repository.criar_usuario(
            nome = dados['nome'],
            email = dados['email'],
            senha = dados['senha']
        )
        return usuario.to_dict()
    

    def autenticar(self, dados):
        usuario = self.usuario_repository.buscar_por_email(dados["email"])
        if usuario and usuario["senha"] == dados["senha"]:
            return usuario
        return None