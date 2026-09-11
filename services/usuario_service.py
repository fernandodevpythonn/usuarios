import bcrypt

class UsuarioService:
    def __init__(self,repository):
        self.reposotory = repository

    def autenticar(self, usuario, senha):
        resultado = self.repository.buscar_por_usuario(
            usuario
        )

        if not resultado:
            return None
        
        usuario_id = resultado[0]
        nome_usuario = resultado[1]
        email = resultado[2]
        senha_hash = resultado[3]
        perfil = resultado[4]

        senha_valida = bcrypt.checkpw(senha.encode(),(senha.encode()))

        if not senha_valida:
            return None
        
        return {
            "id": usuario_id,
            "nome": nome_usuario,
            "email": email,
            "perfil": perfil
        }
    def cadastrar(self,usuario,senha,perfil="usuario"):
        if self.reposotory.existe(usuario):
            raise ValueError("usuário já existe")
         
        return self.reposotory.criar(
            usuario = usuario,
            senha = senha,
            perfil = perfil
        )