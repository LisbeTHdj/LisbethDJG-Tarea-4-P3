import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner

class TestCambioIdiomaWikipedia(unittest.TestCase):
    
    def setUp(self):
       
        service = Service(executable_path=r"C:\\Users\\lisbe\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
    
    def test_cambio_idioma(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")  
        
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".central-featured-lang")))
        
        
        language_links = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
        self.assertGreater(len(language_links), 0, "La lista de idiomas no está visible")
        
        
        english_button = driver.find_element(By.XPATH, "//strong[text()='English']")
        english_button.click()  
        
        
        WebDriverWait(driver, 10).until(EC.url_contains("en.wikipedia.org"))
        
        
        self.assertIn("en.wikipedia.org", driver.current_url, "El idioma no cambió correctamente a Inglés")
        
        
        screenshot_path = os.path.join(os.getcwd(), "wikipedia_english.png")
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")

    def tearDown(self):
        
        self.driver.quit()


if not os.path.exists('reportes'):
    os.makedirs('reportes')


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes", 
            report_name="Reporte_TestCambioIdiomaWikipedia",
            report_title="Resultados de Prueba - Cambio de Idioma en Wikipedia"
        )
    )
