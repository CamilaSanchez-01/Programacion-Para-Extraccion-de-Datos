# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 23 de febrero de 2025

# Librerias
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Parametros de la pagina
def amazon(busqueda, paginas):
    driver = ChromeDriverManager().install()
    s = Service(driver)
    opc = Options()
    opc.add_argument('--start-maximized')
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx")
    time.sleep(9)

    # Buscar elementos
    txtButtomSearch = navegador.find_element(By.ID, "twotabsearchtextbox")
    txtButtomSearch.send_keys("Iphone 15")
    time.sleep(3)
    btnSearchIcon = navegador.find_element(By.ID, "nav-search-submit-button")
    btnSearchIcon.click()
    time.sleep(5)

    # Funcion para imagenes
    for pagina in range(1, paginas+1):
        print(f"imagenes_amazon/{busqueda}_{pagina}.png")
        navegador.save_screenshot(f"imagenes_amazon/{busqueda}_{pagina}.png")
        btnSiguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        btnSiguiente.click()
        time.sleep(6)

    navegador.quit()

if __name__ == "__main__":
    busqueda = "Amazon"
    paginas = 3
    amazon(busqueda, paginas)
