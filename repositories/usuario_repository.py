from database.connection import BancoMysql

class UsuarioRepository:
    def __init__(self,banco):
        self.db = banco
    
    def buscar_por_usuario(self,usuario):
        return self.db.consultar_um(
         """
         SELECT 
           id,
           nome,
           email,
           senha,
           perfil
         FROM usuarios
         WHERE nome = %s
         """,(usuario,)
        )
    
    def buscar_por_id(self,usuario_id):
        return self.db.consultar_um(
        """
          SELECT 
            id,
            nome,
            email,
            perfil
          FROM usuarios
          WHERE id = %s
        """, (usuario_id)
        )
    
    def listar_todos(self):
        return self.db.consultar(
         """
         SELECT 
           id,
           nome,
           email,
           senha,
           perfil
         FROM usuarios
         ORDER BY id
         """
        )
    
    def criar(self,nome,email,senha_hash,perfil = "usuario"):
        self.db.executar(
            """
            INSERT INTO usuarios
            (
               nome,
               email,
               senha,
               perfil
            )
            VALUES
            (
              %s,
              %s,
              %s,
              %s
            )
            """,
            (
                 nome,
                 email,
                 senha_hash,
                 perfil
            )
        )
        return self.db.cursor.lastrowid
