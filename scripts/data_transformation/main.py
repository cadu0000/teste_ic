import os
from dotenv import load_dotenv
from data_transformation import DataSaver, DataTransformer, PDFTableExtractor

if __name__ == "__main__":
    load_dotenv()
    file_name = "Anexo_I.pdf"
    pdf_path = os.path.join(os.getenv("DOWNLOAD_DIR"), file_name)
    name = "Carlos_Eduardo_Pinheiro"

    try:
        extractor = PDFTableExtractor(pdf_path)
        df = extractor.extract_table('3-181')
        
        transformer = DataTransformer()
        df = transformer.replace_abbreviations(df)
        
        saver = DataSaver('data_transformation/data')
        zip_path = saver.save_and_zip(df, name)
    
    except Exception as e:
        print(f"\nErro: {str(e)}")
