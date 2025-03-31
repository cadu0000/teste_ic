from infra.repository import database_manager
from infra.repository.mysql.representante_repository import RepresentanteRepository

class RepresentanteService:
    def __init__(self):
        self.db = database_manager()
        self.representante_repository = RepresentanteRepository(self.db)
    
    def get_representantes(self, cnpj_operadora=None):
        try:
            if cnpj_operadora:
                return self.get_representante_by_cnpj(cnpj_operadora)
            return self.representante_repository.get_all()
        except Exception as e:
            raise Exception(f"Erro ao buscar representantes: {str(e)}")

    def insert_representante(self, data):
        try:
            self.representante_repository.insert(data)
        except Exception as e:
            raise Exception(f"Erro ao inserir representantes: {str(e)}")

    def get_representante_by_cnpj(self, cnpj_operadora):
        try:
            result = self.representante_repository.get(cnpj_operadora)
            if result:
                return result
            else:
                raise ValueError(f"Nenhum representante encontrado para o CNPJ: {cnpj_operadora}")
        except Exception as e:
            raise Exception(f"Erro ao buscar representante por CNPJ {cnpj_operadora}: {str(e)}")
