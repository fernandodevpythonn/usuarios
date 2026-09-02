from controllers.base_controller import BaseController
from flask import render_template,session,url_for

class LoginController(BaseController):
    def __init__(self,app):
     self.rotas = [
        ('/paginalogin','paginalogin',self.pagina_login),
        ('/paginacadastro','paginacadastro',self.pagina_cadastro),
        ('/entrar','entrar',self.entrar,["post"])
     ]
     super().__init__(app)

    def pagina_login(self):
       return render_template("login_pagina.html")
    
    def pagina_cadastro(self):
       return render_template("cadastro_pagina.html")
    
    def entrar(self):
       pass
    
    def cadastrar(self):
       pass