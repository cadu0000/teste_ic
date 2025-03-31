import os
import pandas as pd

class CSVProcessor:
    def __init__(self, directory, output_file):
        self.directory = directory
        self.output_file = output_file
        self.dataframes = []
        
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Diretório não encontrado: {self.directory}")
    
    def get_csv_files(self):
        csv_files = [f for f in os.listdir(self.directory) if f.endswith('.csv')]
        if not csv_files:
            raise ValueError(f"Nenhum arquivo CSV encontrado no diretório: {self.directory}")
        return csv_files
    
    def process_files(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        
        for i, file in enumerate(self.get_csv_files()):
            file_path = os.path.join(self.directory, file)
            
            try:
                df = pd.read_csv(file_path, sep=';', encoding='utf-8')
                self.dataframes.append(df)
                
                df.to_csv(
                    self.output_file,
                    mode='a',
                    index=False,
                    header=(i == 0),
                    sep=';',
                    encoding='utf-8'
                )
            except Exception as e:
                print(f"Erro ao processar {file}: {str(e)}")
                continue
    
    def get_final_dataframe(self):
        return pd.concat(self.dataframes, ignore_index=True) if self.dataframes else None