import mysql
from infra.repository.sqlconnector import SQLConnector

class DatabaseManager:
    def __init__(self):
        self.conn = SQLConnector()  
        
    def query(self, query, params=None):
        with self.conn.conn.cursor() as cursor:  
            cursor.execute(query, params or ())
            return cursor.fetchall() 
    
    def insert_batch(self, query, data, batch_size=3000):
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            try:
                self.conn.execute_many(query, batch)
                print(f"Inserido lote {i // batch_size + 1}")
            except mysql.connector.Error as err:
                print(f"Erro ao inserir lote {i // batch_size + 1}: {err}")
                continue
    
    def close(self):
        self.conn.close_connection() 
