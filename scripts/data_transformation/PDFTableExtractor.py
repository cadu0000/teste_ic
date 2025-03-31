import tabula

class PDFTableExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def extract_table(self, pages):
        tables = tabula.read_pdf(self.pdf_path, pages=pages, multiple_tables=False)
        
        if not tables:
            raise ValueError("Nenhuma tabela encontrada no PDF.")
        
        return tables[0]