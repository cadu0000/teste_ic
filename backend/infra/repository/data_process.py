from core.domain.contabilidade import Contabilidade
from core.domain.operadora import Operadora

class DataProcessor:
    def __init__(self, operadora_df, contabeis_df):
        self.operadora = Operadora(operadora_df)
        self.contabeis = Contabilidade(contabeis_df)
    
    def process_operadora(self):
        return self.operadora.processar_dados_operadora()
    
    def process_representante(self):
        return self.operadora.processar_representante()
    
    def process_contato(self):
        return self.operadora.processar_contato()
    
    def process_localizacao(self):
        return self.operadora.processar_localizacao()
    
    def process_contabeis(self, valid_reg_ans):
        return self.contabeis.processar_contabeis(valid_reg_ans)
