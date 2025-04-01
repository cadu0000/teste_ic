from infra.repository.database_manager import DatabaseManager

class DemonstracoesContabeisRepository:
    def __init__(self, db_manager: DatabaseManager, data=None):
        self.db_manager = db_manager
        self.data = data

    def insert(self):
        query = """
            INSERT INTO demonstracoes_contabeis (data_inicio_tri, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE vl_saldo_final=VALUES(vl_saldo_final)
        """
        if all(len(item) == 6 for item in self.data):
            self.db_manager.insert_batch(query, self.data)
        else:
            raise ValueError("Os dados não estão no formato correto, cada item precisa ser uma tupla de 6 elementos.")

    def get(self, reg_ans=None):
        query = """
            SELECT data_inicio_tri, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
            FROM demonstracoes_contabeis
        """
        try:
            if reg_ans:
                query += " WHERE reg_ans = %s"
                return self.db_manager.query(query, (reg_ans,))
            return self.db_manager.query(query)
        
        except Exception as e:
            raise Exception(f"Erro ao buscar demonstrações contábeis: {str(e)}")
