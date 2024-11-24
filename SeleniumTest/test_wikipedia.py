import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner

class TestAccesoWikipedia(unittest.TestCase):
    def setUp(self):
       
        service = Service(executable_path=r"C:\\Users\\lisbe\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
    
    def test_acceso_wikipedia(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")

        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "searchInput")))

       
        search_bar = driver.find_element(By.ID, "searchInput")
        self.assertTrue(search_bar.is_displayed(), "La barra de búsqueda no está visible")

        
        if not os.path.exists('imagenes'):
            os.makedirs('imagenes')

        
        screenshot_path = os.path.join('imagenes', "wikipedia_homepage.png")
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")

        
        self.assertIn("Wikipedia", driver.title)

       
        language_links = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
        self.assertGreater(len(language_links), 0, "No se encontraron enlaces de idiomas en la página")

    def tearDown(self):
        
        self.driver.quit()


if not os.path.exists('reportes'):
    os.makedirs('reportes')


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",  
            report_name="Reporte_TestAccesoWikipedia",
            report_title="Resultados de Prueba - Acceso a Wikipedia"
        )
    )