from infra.repository import database_manager
from infra.repository.mysql.contato_repository import ContatoRepository

class ContatoService:
    def __init__(self):
        self.db = database_manager()
        self.contato_repository = ContatoRepository(self.db)
    
    def get_contatos(self, cnpj_operadora=None):
        try:
            if cnpj_operadora:
                return self.get_contato_by_cnpj(cnpj_operadora)
            return self.contato_repository.get_all()
        except Exception as e:
            raise Exception(f"Erro ao buscar contatos: {str(e)}")

    def insert_contato(self, data):
        try:
            self.contato_repository.insert(data)
        except Exception as e:
            raise Exception(f"Erro ao inserir contatos: {str(e)}")

    def get_contato_by_cnpj(self, cnpj_operadora):
        try:
            result = self.contato_repository.get(cnpj_operadora)
            if result:
                return result
            else:
                raise ValueError(f"Nenhum contato encontrado para o CNPJ: {cnpj_operadora}")
        except Exception as e:
            raise Exception(f"Erro ao buscar contato por CNPJ {cnpj_operadora}: {str(e)}")
