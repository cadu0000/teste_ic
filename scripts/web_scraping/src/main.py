import os
from dotenv import load_dotenv
from scraper.pdf_scraper import PDFScraper
from downloader.pdf_downloader import PDFDownloader

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    dir = os.getenv("DOWNLOAD_DIR")
    
    os.makedirs(dir, exist_ok=True)

    try:
        scraper = PDFScraper(url)
        pdf_links = scraper.obter_links_pdfs()
        downloader = PDFDownloader(dir)

        for file_name, pdf_url in pdf_links.items():
            file_path = os.path.join(dir, file_name)  
            downloader.download(pdf_url, file_path)

        zip_path = downloader.zip_project("anexos.zip")
        
    except Exception as e:
        print(f"\nErro: {str(e)}")
  
 
