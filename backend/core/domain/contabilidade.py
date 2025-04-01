import pandas as pd

class Contabilidade:
    def __init__(self, contabeis_df):
        self.df = contabeis_df.fillna('')

    def processar_contabeis(self, valid_reg_ans):
        self.df.columns = self.df.columns.str.strip().str.replace('"', '')
        self.df = self.df.loc[:, ~self.df.columns.duplicated()]
        self.df = self.df[self.df['REG_ANS'].isin(valid_reg_ans)]
        
        self.df['CD_CONTA_CONTABIL'] = self.df['CD_CONTA_CONTABIL'].apply(lambda x: str(x)[:20])
        print(self.df.columns)
        self.df['DATA'] = self.df['DATA'].str.replace('"', '')  
        self.df['DATA'] = pd.to_datetime(self.df['DATA'], errors='coerce')
        self.df['VL_SALDO_INICIAL'] = self.df['VL_SALDO_INICIAL'].replace({',': '.'}, regex=True)
        self.df['VL_SALDO_FINAL'] = self.df['VL_SALDO_FINAL'].replace({',': '.'}, regex=True)
        self.df['VL_SALDO_INICIAL'] = pd.to_numeric(self.df['VL_SALDO_INICIAL'], errors='coerce').fillna(0)
        self.df['VL_SALDO_FINAL'] = pd.to_numeric(self.df['VL_SALDO_FINAL'], errors='coerce').fillna(0)
                
        return self.df
