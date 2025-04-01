import pandas as pd

class Operadora:
    def __init__(self, operadora_df):
        self.df = operadora_df.fillna('')

    def processar_dados_operadora(self):
        self.df['Data_Registro_ANS'] = self.df['Data_Registro_ANS'].astype(str).str.replace('"', '', regex=False)
        self.df['CNPJ'] = self.df['CNPJ'].apply(lambda x: str(x).zfill(14) if pd.notna(x) else '000000000000')
        self.df['Data_Registro_ANS'] = self.df['Data_Registro_ANS'].str.replace('"', '', regex=False)
        self.df['Data_Registro_ANS'] = pd.to_datetime(self.df['Data_Registro_ANS'], format='%Y-%m-%d')
        return self.df[['CNPJ', 'Registro_ANS', 'Razao_Social', 'Nome_Fantasia', 'Modalidade', 
                        'Endereco_eletronico', 'Regiao_de_Comercializacao', 'Data_Registro_ANS']]
    
    def processar_representante(self):
        self.df['CNPJ'] = self.df['CNPJ'].apply(lambda x: str(x).zfill(14) if pd.notna(x) else '000000000000')
        return self.df[['CNPJ', 'Representante', 'Cargo_Representante']]
    
    def processar_contato(self):
        self.df['CNPJ'] = self.df['CNPJ'].apply(lambda x: str(x).zfill(14) if pd.notna(x) else '000000000000')
        df_telefone = self.df[['CNPJ', 'DDD', 'Telefone']].rename(columns={'Telefone': 'Numero'})
        df_fax = self.df[['CNPJ', 'DDD', 'Fax']].rename(columns={'Fax': 'Numero'})
        self.df['Numero'] = self.df['Numero'].apply(lambda x: str(x)[:11] if pd.notna(x) else '')
        df_telefone['tipo'] = 'Telefone'
        df_fax['tipo'] = 'Fax'
        df_contato = pd.concat([df_telefone, df_fax]).dropna(subset=['Numero'])
        df_contato['DDD'] = df_contato['DDD'].apply(lambda x: x.replace('"', '') if pd.notna(x) and x != '' else '00')
        
        return df_contato
    
    def processar_localizacao(self):
        self.df['CNPJ'] = self.df['CNPJ'].apply(lambda x: str(x).zfill(14) if pd.notna(x) else '000000000000')
        self.df['UF'] = self.df['UF'].apply(lambda x: str(x).strip()[:2] if pd.notna(x) else '00')
        return self.df[['Logradouro', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP', 'CNPJ',]]
