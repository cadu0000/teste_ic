from infra.repository.database_manager import DatabaseManager

class RepresentanteRepository:
    def __init__(self, db_manager: DatabaseManager, data):
        self.db_manager = db_manager
        self.data = data

    def insert(self):
        query = """
            INSERT INTO representante (cnpj_operadora, representante, cargo_representante)
            VALUES (%s, %s, %s)
        """
        self.db_manager.insert_batch(query, self.data)
        
    def get(self, cnpj_operadora=None):
        query = """
            SELECT cnpj_operadora, representante, cargo_representante
            FROM representante
        """
        try:
            if cnpj_operadora:
                query += " WHERE cnpj_operadora = %s"
                return self.db_manager.query(query, (cnpj_operadora,))
            return self.db_manager.query(query)
  
        except Exception as e:
            print(f"Erro ao buscar representante: {str(e)}")
