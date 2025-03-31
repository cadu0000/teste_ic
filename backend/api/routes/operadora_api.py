from api.handlers.operadora_handler import OperadoraHandler

class OperadoraAPI:
    def __init__(self, app):
        self.app = app
        self.operadora_handler = OperadoraHandler()
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/operadoras-com-maiores-despesas', 'list_operadoras_with_highest_expenses', self.operadora_handler.list_operadoras_with_highest_expenses, methods=['GET'])
        self.app.add_url_rule('/operadora', 'search_operadora_by_name', self.operadora_handler.search_operadora_by_name, methods=['GET'])

    def home(self):
        return 'Bem-vindo à API de operadoras de saúde'
