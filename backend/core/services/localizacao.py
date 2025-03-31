from infra.repository import database_manager
from infra.repository.mysql.localizacao_repository import LocalizacaoRepository

class LocalizacaoService:
    def __init__(self):
        self.db = database_manager()
        self.localizacao_repository = LocalizacaoRepository(self.db)
    
    def get_localizacoes(self, cnpj_operadora=None):
        try:
            if cnpj_operadora:
                return self.get_localizacao_by_cnpj(cnpj_operadora)
            return self.localizacao_repository.get()
        except Exception as e:
            raise Exception(f"Erro ao buscar localizações: {str(e)}")

    def insert_localizacao(self, data):
        try:
            self.localizacao_repository.insert(data)
        except Exception as e:
            raise Exception(f"Erro ao inserir localizações: {str(e)}")

    def get_localizacao_by_cnpj(self, cnpj_operadora):
        try:
            result = self.localizacao_repository.get(cnpj_operadora)
            if result:
                return result
            else:
                raise ValueError(f"Nenhuma localização encontrada para o CNPJ: {cnpj_operadora}")
        except Exception as e:
            raise Exception(f"Erro ao buscar localização por CNPJ {cnpj_operadora}: {str(e)}")
