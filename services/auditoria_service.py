from datetime import datetime

class AuditoriaService:
    def __init__(self,repository):
        self.repository = repository

    def registrar(self,usuario_id,acao,entidade,entidade_id=None,descricao=None,ip=None):
        self.repository.registrar(
            usuario_id=usuario_id,
            acao=acao,
            entidade=entidade,
            entidade_id=entidade_id,
            descricao=descricao,
            ip=ip
        )

    def listar(
            self,
            acao=None,
            entidade=None,
            usuario_id=None
    ):
        
        auditorias = self.repository.listar(
            acao=acao,
            entidade=entidade,
            usuario_id=usuario_id
        )

        resultado = []

        for auditoria in auditorias:

                auditoria = list(auditoria)

                data_hora = auditoria[8]

                if isinstance(data_hora, str):
                    data_hora = datetime.strptime(
                        data_hora,
                        "%Y-%m-%d %H:%M:%S"
                    )

                auditoria[8] = data_hora.strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

                resultado.append(tuple(auditoria))

        return resultado