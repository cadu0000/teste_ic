import os
import zipfile

class DataSaver:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def save_and_zip(self, df, name):
        csv_path = os.path.join(self.output_dir, f'{name}_Procedimentos_Eventos_Saude.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"CSV salvo em: {csv_path}")
        
        zip_path = os.path.join(self.output_dir, f'Teste_{name}.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        
        return zip_path