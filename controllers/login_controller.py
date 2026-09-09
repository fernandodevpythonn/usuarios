from controllers.base_controller import BaseController
from flask import render_template,session,url_for,request
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from database.connection import mysql


class LoginController(BaseController):
    def __init__(self,app):
     self.rotas = [
        ('/paginalogin','paginalogin',self.pagina_login),
        ('/paginacadastro','paginacadastro',self.pagina_cadastro),
        ('/entrar','entrar',self.entrar,['POST']),
        ('/registrar','registrar',self.cadastrar,['POST'])
     ]
     self.usuarios = [{"email":"fernando@gmail.com","senha":"12345"}]

     super().__init__(app)

     self.db = mysql()
     self.usuario_repository = UsuarioRepository(self.db)
     self.usuario_service = UsuarioService(self.usuario_repository)

     

    def pagina_login(self):
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
    
    def cadastrar(self):
       pass