from flask import jsonify, request
from core.services.operadora import OperadoraService

class OperadoraHandler:
    def __init__(self):
        self.operadora_service = OperadoraService()
        
    def list_operadoras_with_highest_expenses(self):
        try:
            operadoras = self.operadora_service.get_operadoras_with_highest_expenses()  

            if not operadoras:
                return jsonify({"message": "Não foram encontrados operadores"}), 404
            
            return jsonify(operadoras), 200
        except Exception as e:
            return jsonify({"error": f"Error listing operadoras: {str(e)}"}), 500

    def search_operadora_by_name(self):
        try:
            name = request.args.get('name')
            if not name:
                return jsonify({"error": "é necessário preencher o campo nome"}), 400
            
            operadora = self.operadora_service.get_operadora_by_name(name)

            if not operadora:
                return jsonify({"message": "Não foram encontrados operadores"}), 404

            return jsonify(operadora), 200
        
        except Exception as e:
            return jsonify({"error": f"Erro ao procurar pela operadora '{name}': {str(e)}"}), 500
