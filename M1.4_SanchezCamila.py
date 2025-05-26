# Alumna: Sanchez Parra Camila Grupo: 951
# Fecha de realizacion: 2 de marzo de 2025

#librerias
import requests
import pandas as pd
from bs4 import  BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
    btnSearchIcon = navegador.find_element(By.ID, "nav-search-submit-button")
    txtButtomSearch.send_keys(busqueda)
    time.sleep(7)
    btnSearchIcon.click()
    time.sleep(5)



    productos = []

    for paginas in range(1, paginas + 1):
        time.sleep(7)
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        items = soup.find_all("div", {"data-component-type": "s-search-result"})

        for item in items [:4]:

            nombre_element = item.find("h2", class_= "a-size-base-plus a-spacing-none a-color-base a-text-normal")
            if nombre_element and nombre_element.find_all("span"):
                nombre = nombre_element.find("span").text.strip()

            else:
                nombre = "No Disponible"

            price_element = item.find("span", class_= "a-price-whole")
            if price_element:
                precio = price_element.text.strip()

            else:
                precio = "No Disponible"

            rank_element = item.find("span", class_= "a-icon-alt")
            if rank_element:
                ranking = rank_element.text.strip()

            else:
                ranking = "No Cuenta Con Calificaciones"

            entrega_element = item.find("span", class_= "a-color-base a-text-bold")
            if entrega_element:
                fecha_entrega = entrega_element.text.strip()

            else:
                fecha_entrega = "No Disponible"

            productos.append([nombre,precio, ranking, fecha_entrega])

        navegador.save_screenshot(f"imagenes/{busqueda}_{paginas}.png")

        btnSiguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        if btnSiguiente:
            btnSiguiente.click()
            time.sleep(6)
        else:
            print("No se encuentran mas paginas de productos")
            break


    navegador.quit()
    df = pd.DataFrame(productos, columns=["Nombre", "Precio", "Ranking", "Fecha de entrega"])
    df.to_csv(f"dataset/{busqueda}_productos.csv")



if __name__ == "__main__":
    busqueda = "macbook"
    paginas = 3
    amazon(busqueda, paginas)
