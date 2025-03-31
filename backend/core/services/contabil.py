from infra.repository import database_manager
from infra.repository.mysql.demonstracoes_contabeis_repository import DemonstracoesContabeisRepository

class DemonstracoesContabilService:
    def __init__(self):
        self.db = database_manager()
        self.contabil_repository = DemonstracoesContabeisRepository(self.db)
    
    def get_demonstracoes_contabeis(self, reg_ans=None):
        try:
            if reg_ans:
                return self.get_demonstracao_by_reg_ans.get(reg_ans)
            return self.contabil_repository.get()
        except Exception as e:
            raise Exception(f"Erro ao buscar demonstrações contábeis: {str(e)}")

    def insert_demonstracoes_contabeis(self, data):
        try:
            self.contabil_repository.insert(data)
        except Exception as e:
            raise Exception(f"Erro ao inserir demonstrações contábeis: {str(e)}")

    def get_demonstracao_by_reg_ans(self, reg_ans):
        try:
            result = self.contabil_repository.get(reg_ans)
            if result:
                return result
            else:
                raise ValueError(f"Nenhuma demonstração contábil encontrada para o reg_ans: {reg_ans}")
        except Exception as e:
            raise Exception(f"Erro ao buscar demonstração contábil por reg_ans {reg_ans}: {str(e)}")
