from flask import Flask
from flask_cors import CORS
from api.routes.operadora_api import OperadoraAPI
from core.services.data_ingestion import RawDataIngestion
from infra.repository.sqlconnector import SQLConnector

app = Flask(__name__)
CORS(app)  

tarefa_api = OperadoraAPI(app)

@app.teardown_appcontext
def teardown(exception):
    db = SQLConnector()
    db.close_connection() 

if __name__ == '__main__':
    ## execução do script de ingestão dos dados .csv
    # ingest = RawDataIngestion()
    # ingest.run()
    app.run(debug=True)
