import os
import zipfile
import requests

class PDFDownloader:
    def __init__(self, dir):  
        self.dir = os.path.abspath(dir)
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def download(self, pdf_url, file_name):
        file_name = os.path.basename(file_name)
        file_path = os.path.join(self.dir, file_name)  
        response = requests.get(pdf_url)
        
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
        else:
            raise ValueError(f"Erro ao baixar {file_name}: {response.status_code}")

    def zip_project(self, zip_name):
        zip_path = os.path.join(self.dir, zip_name)  
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.dir):
                for file in files:
                    if file != zip_name: 
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.dir)
                        zipf.write(file_path, arcname)