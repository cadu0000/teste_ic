from infra.repository.database_manager import DatabaseManager
from infra.repository.mysql.operadora_repository import OperadoraRepository

class OperadoraService:
    def __init__(self):
        self.db = DatabaseManager()
        self.operadora_repository = OperadoraRepository(self.db)
    
    def get_operadoras(self, cnpj=None):
        try:
            if cnpj:
                return self.get_operadora_by_cnpj(cnpj)
            return self.operadora_repository.get()
        except Exception as e:
            raise Exception(f"Erro ao buscar operadoras: {str(e)}")

    def insert_operadora(self, data):
        try:
            self.operadora_repository.insert(data)
        except Exception as e:
            raise Exception(f"Erro ao inserir operadoras: {str(e)}")

    def get_operadora_by_cnpj(self, cnpj):
        try:
            result = self.operadora_repository.get(cnpj)
            if result:
                return result
            else:
                raise ValueError(f"Nenhuma operadora encontrada para o CNPJ: {cnpj}")
        except Exception as e:
            raise Exception(f"Erro ao buscar operadora por CNPJ {cnpj}: {str(e)}")
        
    def get_operadora_by_name(self, name):
        try:
            result = self.operadora_repository.get_operadora_by_name(name)
            if result:
                return result
            else:
                raise ValueError(f"Nenhuma operadora encontrada para o name: {name}")
        except Exception as e:
            raise Exception(f"Erro ao buscar operadora por name {name}: {str(e)}")
        
    def get_operadoras_with_highest_expenses(self):
        try:
            result = self.operadora_repository.get_operadoras_with_highest_expenses()
            return result
        except Exception as e:
            raise Exception({str(e)})
