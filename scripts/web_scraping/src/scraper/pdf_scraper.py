from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PDFScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def obter_links_pdfs(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 2) 

        try:
            anexo1 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Anexo I')]")))
            anexo2 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Anexo II')]")))

            pdf_links = {
                "Anexo_I.pdf": anexo1.get_attribute("href"),
                "Anexo_II.pdf": anexo2.get_attribute("href"),
            }

        except Exception as e:
            raise ValueError(f"Erro ao encontrar os PDFs: {e}")
        
        self.driver.quit()
        return pdf_links