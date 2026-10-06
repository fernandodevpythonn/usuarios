from flask import render_template, request, redirect, url_for, session

from controllers.base_controller import BaseController

from database.connection import BancoMysql

from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from repositories.auditoria_repository import AuditoriaRepository
from services.auditoria_service import AuditoriaService

class UsuarioController(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/usuarios','usuarios', self.listar,['GET'],'administrador'),
            ('/usuarios/cadastrar', 'cadastrar_usuario',self.cadastrar,['GET', 'POST'], 'administrador'),
            ('/usuarios/editar/<int:usuario_id>','editar_usuario',self.editar,['GET','POST'],'administrador'),
            ('/usuarios/excluir/<int:usuario_id>','excluir_usuario',self.excluir,['POST'],'administrador'),
            ('/usuarios/excluir/<int:usuario_id>','confirmar_exclusao_usuario',self.confirmar_exclusao,['GET'],'administrador'),
            ('/perfil','perfil',self.editar_perfil,['GET','POST'],'autenticado')

        ]

        super().__init__(app)

        self.db = BancoMysql()
        self.repository_usuario = UsuarioRepository(self.db)
        self.usuario_service = UsuarioService(self.repository_usuario)
        self.auditoria_repository = AuditoriaRepository(self.db)
        self.auditoria_service = AuditoriaService(self.auditoria_repository)

    def listar(self):
            usuarios = self.usuario_service.listar_todos()
            return render_template("html_usuarios/usuarios.html", usuarios=usuarios)
    
    def cadastrar(self):
            if request.method == 'POST':

             nome_usuario = request.form.get("usuario")
             senha = request.form.get("senha")
             confirmar_senha = request.form.get("confirmar_senha")
             data_nascimento = request.form.get("nascimento")
             perfil = request.form.get("perfil")


             if (
                not nome_usuario
                or not senha
                or not confirmar_senha
                or not data_nascimento
                or not perfil
             ):

                return render_template(
                    "html_usuarios/cadastrar.html",
                    erro="Preencha todos os campos.",
                    dados=request.form
                )


             if senha != confirmar_senha:

                return render_template(
                    "html_usuarios/cadastrar.html",
                    erro="As senhas não coincidem.",
                    dados=request.form
                )


             try:

                usuario_id = self.usuario_service.cadastrar(

                    usuario=nome_usuario,

                    senha=senha,

                    data_nascimento=data_nascimento,

                    perfil=perfil
                )


                self.auditoria_service.registrar(

                    usuario_id=session.get("usuario_id"),

                    acao="CADASTRO",

                    entidade="USUARIO",

                    entidade_id=usuario_id,

                    descricao="Usuário cadastrado pelo administrador",

                    ip=request.remote_addr
                )


             except ValueError as e:

                return render_template(
                    "html_usuarios/cadastrar.html",
                    erro=str(e),
                    dados=request.form
                )


             return redirect(
                url_for("usuarios")
              )


            return render_template(
            "html_usuarios/cadastrar.html"
           )
    def editar(self):
         pass
    def excluir(self):
         pass
    def confirmar_exclusao(self):
         pass
    def editar_perfil(self):
         pass