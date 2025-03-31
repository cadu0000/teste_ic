import pandas as pd

class Contabilidade:
    def __init__(self, contabeis_df):
        self.df = contabeis_df.fillna('')

    def processar_contabeis(self):
        valid_reg_ans = self.df['REG_ANS']
        df_contabeis = self.df[self.df['REG_ANS'].isin(valid_reg_ans)]
        df_contabeis['VL_SALDO_INICIAL'] = pd.to_numeric(df_contabeis['VL_SALDO_INICIAL'].str.replace(',', '.'), errors='coerce')
        df_contabeis['VL_SALDO_FINAL'] = pd.to_numeric(df_contabeis['VL_SALDO_FINAL'].str.replace(',', '.'), errors='coerce')
        return df_contabeis
