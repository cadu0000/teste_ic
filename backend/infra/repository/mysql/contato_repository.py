from main import DatabaseManager

class ContatoRepository:
    def __init__(self, db_manager: DatabaseManager, data=None):
        self.db_manager = db_manager
        self.data = data

    def insert(self):
        query = """
            INSERT INTO contato (cnpj_operadora, tipo, ddd, numero)
            VALUES (%s, %s, %s, %s)
        """
        self.db_manager.insert_batch(query, self.data)

    def get(self, cnpj_operadora=None):
        query = """
            SELECT cnpj_operadora, tipo, ddd, numero
            FROM contato
        """
        try:
            if cnpj_operadora:
                query += " WHERE cnpj_operadora = %s"
                return self.db_manager.query(query, (cnpj_operadora,))
            return self.db_manager.query(query)
        
        except Exception as e:
            print(f"Erro ao buscar contato: {str(e)}")
