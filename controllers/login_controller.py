from controllers.base_controller import BaseController
from flask import render_template,session,url_for,request,redirect
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from database.connection import BancoMysql


class LoginController(BaseController):
    def __init__(self,app):
     self.rotas = [
        ('/paginalogin','paginalogin',self.pagina_login),
        ('/paginacadastro','paginacadastro',self.pagina_cadastro),
        ('/entrar','entrar',self.entrar,['POST']),
        ('/registrar','registrar',self.registrar,['POST']),
     ]

     super().__init__(app)

     self.db = BancoMysql()
     self.usuario_repository = UsuarioRepository(self.db)
     self.usuario_service = UsuarioService(self.usuario_repository)

    def pagina_login(self):
       if session.get("usuario_logado"):
          return redirect(url_for("home"))
       
       return render_template("login_pagina.html")
    
    def pagina_cadastro(self):
       return render_template("cadastro_pagina.html")
    
    def entrar(self):
       usuario = request.form.get("usuario")
       senha = request.form.get("senha")

       if not usuario or not senha:
          erro = "preencha o usuario e senha."

          return render_template(
             "login_pagina.html", erro = erro
          )
       
       usuario_valido = self.usuario_service.autenticar(usuario,senha)
       if usuario_valido:
          session["usuario_logado"] = True
          session["usuario_id"] = usuario_valido["id"]
          session["usuario"] = usuario_valido["usuario"]
          session["perfil_logado"] = usuario_valido["perfil"]

          return redirect(
             url_for("home")
          )

    def registrar(self):
       usuario = request.form.get("usuario")
       senha = request.form.get("senha")

       if not usuario or not senha:
          erro = "usuário e senha são obrigatórios"

          return render_template("cadastro_pagina.html",erro=erro)
       
       try:
          usuario_id = self.usuario_service.cadastrar(
             usuario = usuario,
             senha = senha,
             perfil = "usuario"
          )
       except ValueError as e:
          return render_template("cadastro_pagina.html",erro=str(e))
       
       sucesso = "cadastro realizado, faça login."
       
       return render_template("login_pagina.html",sucesso=sucesso)