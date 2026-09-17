
class BancoTabelas:
    def __init__(self,banco):
        self.banco = banco

    def criar_tabelas(self):
        self.criar_tabela_usuarios()
        self.criar_tabela_auditoria()

    def criar_tabela_usuarios(self):
        self.banco.executar("""
           CREATE TABLE IF NOT EXISTS usuarios (
             id INT AUTO_INCREMENT PRIMARY KEY,
             nome VARCHAR(255) NOT NULL,
             senha VARCHAR(255) NOT NULL,
             perfil VARCHAR(50) NOT NULL DEFAULT 'usuario'
           )
        """)

    def criar_tabela_auditoria(self):
        self.banco.executar("""
            CREATE TABLE IF NOT EXISTS auditoria (
             id INT AUTO_INCREMENT PRIMARY KEY,
             usuario_id INT NULL,
             acao VARCHAR(50) NOT NULL,
             entidade VARCHAR(50) NOT NULL,
             entidade_id INT NULL,
             descricao VARCHAR(255),
             ip VARCHAR(45),
             data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (usuario_id)          
                REFERENCES usuarios(id)
                ON DELETE SET NULL
            )
        """)