import os
import dotenv
import mysql.connector

class SQLConnector:
    def __init__(self):
        try:
            dotenv.load_dotenv()
            self.conn = mysql.connector.connect(
                host="localhost",
                user=os.getenv("USER_LOGIN"),
                password=os.getenv("USER_PASSWORD"),
                database=os.getenv("DATABASE_NAME"),
                connection_timeout=600
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            exit(1)
    
    def execute_many(self, query, values_list):
        try:
            self.cursor.executemany(query, values_list)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao executar múltiplas inserções: {err}")

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except mysql.connector.Error as err:
            print(f"Erro ao fechar conexão com o banco: {err}")
