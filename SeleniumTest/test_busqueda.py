import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner
from datetime import datetime

class TestBusquedaWikipedia(unittest.TestCase):
    def setUp(self):
       
        service = Service(executable_path=r"C:\\Users\\lisbe\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()

    def test_busqueda_juan_pablo_duarte(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")

        wait = WebDriverWait(driver, 10)
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
            self.assertTrue(search_box.is_displayed(), "Criterio de aceptación 1: La barra de búsqueda no está visible o no es interactuable.")
            print("Criterio de aceptación 1: La barra de búsqueda está visible y es interactuable.")
        except Exception as e:
            self.fail(f"Criterio de rechazo 1: No se puede interactuar con la barra de búsqueda. Detalle: {e}")
            return

        
        search_term = "Juan Pablo Duarte"
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        
        try:
            result_heading = wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
            self.assertIn(search_term, result_heading.text, 
                          f"Criterio de aceptación 2: El resultado no corresponde al término buscado '{search_term}'.")
            print(f"Criterio de aceptación 2: El encabezado contiene el término '{search_term}'.")
        except Exception as e:
            self.fail(f"Criterio de rechazo 2: No se encontraron resultados relacionados. Detalle: {e}")
            return

        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = 'imagenes'
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"resultado_busqueda_{timestamp}.png")
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
            report_name="Reporte_TestBusquedaWikipedia",
            report_title="Resultados de Prueba - Búsqueda en Wikipedia"
        )
    )
