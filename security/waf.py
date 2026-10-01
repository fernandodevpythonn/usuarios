from flask import request

from security.brasil_ip import ValidarIP

def configurar_waf(app):
    Validar_ip = ValidarIP()

    @app.before_request
    def verificar_ip():
        ip