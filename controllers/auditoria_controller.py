from flask import render_template,request
from controllers.base_controller import BaseController
from database.connection import BancoMysql
from repositories.auditoria_repository import AuditoriaRepository
from services.auditoria_service import AuditoriaService

class AuditoriaController(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/auditoria','auditoria',self.listar,['GET'],'administrador'),
        ]

        super().__init__(app)
        self.db = BancoMysql()
        self.auditoria_repository = AuditoriaRepository(self.db)
        self.auditoria_service = AuditoriaService(self.auditoria_repository)

    def listar(self):
        # acao = request.args.get("acao")
        # entidade = request.args.get("entidade")
        # usuario_id = request.args.get("usuario_id")
        # auditorias = self.auditoria_service.listar(acao=acao,entidade=entidade,usuario_id=usuario_id)
        # return render_template("html_auditoria/auditoria.html", auditorias=auditorias,acao=acao,entidade=entidade,usuario_id=usuario_id)
        return render_template("html_auditoria/auditoria.html")
    
    