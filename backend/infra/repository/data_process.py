from core.domain.contabilidade import Contabilidade
from core.domain.operadora import Operadora

class DataProcessor:
    def __init__(self, operadora_df, contabeis_df):
        self.operadora = Operadora(operadora_df)
        self.contabeis = Contabilidade(contabeis_df)
    
    def processar_operadora(self):
        return self.operadora.processar_dados_operadora()
    
    def processar_representante(self):
        return self.operadora.processar_representante()
    
    def processar_contato(self):
        return self.operadora.processar_contato()
    
    def processar_localizacao(self):
        return self.operadora.processar_localizacao()
    
    def processar_contabeis(self):
        return self.contabeis.processar_contabeis()
