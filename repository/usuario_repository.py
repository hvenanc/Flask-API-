from config.firebase_config import db
from models.usuario import Usuario

class UsuarioRepositoty:

    def __init__(self):
        self.collection = db.collection("usuarios")


    def criar_usuario(self, nome, email, senha):
        doc = self.collection.document()
        usuario = Usuario(
            id = doc.id,
            nome = nome,
            email = email,
            senha = senha
        )
        doc.set(usuario.to_dict())
        return usuario
    

    def buscar_por_email(self, email):
        docs = self.collection.where("email", "==", email).stream()
        for doc in docs:
            return doc.to_dict()
        return None
        