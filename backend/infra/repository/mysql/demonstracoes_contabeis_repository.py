from main import DatabaseManager

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
        self.db_manager.insert_batch(query, self.data)

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
            print(f"Erro ao buscar demonstrações contábeis: {str(e)}")
