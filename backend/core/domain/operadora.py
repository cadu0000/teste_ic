import pandas as pd

class Operadora:
    def __init__(self, operadora_df):
        self.df = operadora_df.fillna('')

    def processar_dados_operadora(self):
        return self.df[['CNPJ', 'Registro_ANS', 'Razao_Social', 'Nome_Fantasia', 'Modalidade', 
                        'Endereco_eletronico', 'Regiao_de_Comercializacao', 'Data_Registro_ANS']]
    
    def processar_representante(self):
        return self.df[['CNPJ', 'Representante', 'Cargo_Representante']]
    
    def processar_contato(self):
        df_telefone = self.df[['CNPJ', 'DDD', 'Telefone']].rename(columns={'Telefone': 'Numero'})
        df_fax = self.df[['CNPJ', 'DDD', 'Fax']].rename(columns={'Fax': 'Numero'})
        df_telefone['tipo'] = 'Telefone'
        df_fax['tipo'] = 'Fax'
        df_contato = pd.concat([df_telefone, df_fax]).dropna(subset=['Numero'])
        df_contato['DDD'] = df_contato['DDD'].apply(lambda x: str(int(x)) if pd.notna(x) else '00')
        return df_contato
    
    def processar_localizacao(self):
        return self.df[['CNPJ', 'Logradouro', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP']]
