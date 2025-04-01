from infra.repository.database_manager import DatabaseManager

class OperadoraRepository:
    def __init__(self, db_manager: DatabaseManager, data=None):
        self.db_manager = db_manager
        self.data = data

    def insert(self):
        query = """
            INSERT INTO operadora (cnpj, reg_ans, razao_social, nome_fantasia, modalidade, endereco_eletronico, 
                                regiao_comercializacao, data_registro_ans)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE reg_ans=VALUES(reg_ans)
        """
        try:
            self.db_manager.insert_batch(query, self.data)
            return 200
        except Exception as e:
            return {"error": "Erro ao fazer insert"}, 500

    def get(self, cnpj_operadora=None):
        query = """
            SELECT cnpj, reg_ans, razao_social, nome_fantasia, modalidade, endereco_eletronico, 
                   regiao_comercializacao, data_registro_ans
            FROM operadora
        """
        try:
            if cnpj_operadora:
                query += " WHERE cnpj = %s"
                return self.db_manager.query(query, (cnpj_operadora,)), 200
            return self.db_manager.query(query)
        
        except Exception as e:
            return {"error": "Erro ao buscar operadora"}, 500
            
    def get_operadoras_with_highest_expenses(self):
        query = """
            SELECT nome_fantasia, reg_ans, total_despesas FROM maiores_despesas_ultimo_ano LIMIT 3;
        """
        try:    
            operadoras = self.db_manager.query(query)
            
            if not operadoras:
                return {"message": "Nenhuma operadora encontrada com maiores despesas"}, 404
            return operadoras, 200
        
        except Exception as e:
            raise Exception (f"Erro ao buscar operadoras com maiores despesas: {str(e)}")

    def get_operadora_by_name(self, name):
        if not name:
            return {"error": "Nome da operadora é necessário"}, 400

        query = """
            SELECT nome_fantasia, cnpj
            FROM operadora WHERE nome_fantasia LIKE %s
        """
        try:
            operadoras = self.db_manager.query(query, ('%' + name + '%',))
            if not operadoras:
                return {"message": "Nenhuma operadora encontrada"}, 404
  
            return operadoras, 200 
        except Exception as e:
            raise Exception(f"Erro ao buscar operadora por nome {name}: {str(e)}")