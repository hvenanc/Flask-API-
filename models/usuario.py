from werkzeug.security import check_password_hash

class Usuario:

    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    
    def check_senha(self, senha_digitada):
        return check_password_hash(self.senha, senha_digitada)


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }
    
    @staticmethod
    def to_user(dict):
        return Usuario(
            id = dict["id"],
            nome = dict["nome"],
            email = dict["email"],
            senha = dict["senha"]
        )