from main import DatabaseManager

class LocalizacaoRepository:
    def __init__(self, db_manager: DatabaseManager, data=None):
        self.db_manager = db_manager
        self.data = data

    def insert(self):
        query = """
            INSERT INTO localizacao (cnpj_operadora, logradouro, numero, complemento, bairro, cidade, uf, cep)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.db_manager.insert_batch(query, self.data)

    def get(self, cnpj_operadora=None):
        query = """
            SELECT cnpj_operadora, logradouro, numero, complemento, bairro, cidade, uf, cep
            FROM localizacao
        """
        try:
            if cnpj_operadora:
                query += " WHERE cnpj_operadora = %s"
                return self.db_manager.query(query, (cnpj_operadora,))
            return self.db_manager.query(query)
        
        except Exception as e:
            print(f"Erro ao buscar localização: {str(e)}")
