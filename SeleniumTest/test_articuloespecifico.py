import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner

class TestAccesoArticuloWikipedia(unittest.TestCase):
    
    def setUp(self):
        
        service = Service(executable_path=r"C:\Users\lisbe\Downloads\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
    
    def test_acceso_y_contenido_articulo(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Python_(lenguaje_de_programaci%C3%B3n)")  
        

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstHeading")))  
        
       
        article_title = driver.find_element(By.ID, "firstHeading")
        self.assertTrue(article_title.is_displayed(), "El título del artículo no está visible")
        self.assertIn("Python", article_title.text, "El artículo no corresponde al lenguaje de programación Python")
        
       
        content = driver.find_element(By.ID, "bodyContent")  
        self.assertTrue(content.is_displayed(), "El contenido del artículo no está visible")

        
        images = driver.find_elements(By.TAG_NAME, "img")
        self.assertGreater(len(images), 0, "No se encontraron imágenes en el artículo")

      
        links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
        self.assertGreater(len(links), 0, "El artículo no tiene enlaces a otros artículos relacionados")

       
        driver.set_window_size(375, 667)  
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bodyContent")))
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertTrue(body.is_displayed(), "El cuerpo del artículo no se muestra correctamente en móvil")

        
        screenshot_path = os.path.join(os.getcwd(), "wikipedia_python_article_mobile.png")
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
            report_name="Reporte_TestAccesoArticuloWikipedia",
            report_title="Resultados de Prueba - Acceso al Artículo de Wikipedia"
        )
    )
