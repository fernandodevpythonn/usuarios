import bcrypt

class UsuarioService:
    def __init__(self,repository):
        self.repository = repository

    def autenticar(self, nome, senha):
        resultado = self.repository.buscar_por_usuario(
            nome
        )

        if not resultado:
            return None
        
        usuario_id = resultado[0]
        nome_usuario = resultado[1]
        senha_hash = resultado[2]
        perfil = resultado[3]

        
        
        return {
            "id": usuario_id,
            "nome": nome_usuario,
            "perfil": perfil
        }
    def cadastrar(self,nome,senha,perfil="usuario"):
        if self.repository.existe(nome):
            raise ValueError("usuário já existe")
         
        return self.repository.criar(
            nome = nome,
            senha = senha,
            perfil = perfil
        )