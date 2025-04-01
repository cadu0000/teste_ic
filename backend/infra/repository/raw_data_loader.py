import os
import pandas as pd
import csv

class RawDataLoader:
    def __init__(self, operadora_directory='backend/infra/repository/db/raw_data/operadoras', contabeis_directory='backend/infra/repository/db/raw_data/contabeis'):
        self.operadora_directory = operadora_directory
        self.contabeis_directory = contabeis_directory
        self.operadora_data = self._load_data(self.operadora_directory)
        self.contabeis_data = self._load_data(self.contabeis_directory)

    def _load_data(self, directory):
        files = [f for f in os.listdir(directory) if f.endswith('.csv')]
        dataframes = [pd.read_csv(os.path.join(directory, file), delimiter=';', encoding='ISO-8859-1', quoting=csv.QUOTE_NONE, on_bad_lines='skip') for file in files]
        return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
