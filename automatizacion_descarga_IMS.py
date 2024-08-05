import time
import logging
from tkinter import Tk, Label, Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Configuración de logs
logging.basicConfig(level=logging.INFO, filename='automatizacion_descarga_IMS.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Variables
link = "https://www.gub.uy/instituto-nacional-estadistica/"
search_text = "IMS (Variación 12 meses) Período {:02d}/24".format((datetime.now().month - 2) % 12 or 12)
check_interval = 3600  # 1 hora en segundos

# Ruta al chromedriver
chromedriver_path = r"C:\chromedriver.exe"

# Configuración de las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecuta en modo headless si lo prefieres

# Servicio de ChromeDriver
service = Service(executable_path=chromedriver_path)

# Función para mostrar notificaciones locales
def show_notification(title, message):
    root = Tk()
    root.title(title)
    Label(root, text=message).pack(pady=20)
    Button(root, text="OK", command=root.destroy).pack(pady=10)
    root.mainloop()

# Función para buscar el texto en la página usando Selenium
def check_page_with_selenium(link, search_text):
    logging.info("Iniciando chequeo de la página")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(link)
    
    try:
        # Espera hasta que el contenedor esté presente
        container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/article/div/div[2]/div/div/div[2]/div/div/div[2]/ul/li[3]/a'))
        )
        container_text = container.text
        logging.info(f"Contenido del contenedor: '{container_text}'")
        logging.info(f"Texto buscado: '{search_text}'")
        if search_text in container_text:
            logging.info("Texto encontrado en la página")
            return True
        else:
            logging.info("Texto no encontrado en la página")
            show_notification("IMS Chequeo", "El IMS de este mes aún no está disponible.")
    except Exception as e:
        logging.error(f"Error al chequear la página: {e}")
    finally:
        driver.quit()
    return False

# Función para abrir el navegador y hacer clic en el link de descarga
def open_browser_and_download(link):
    logging.info("Iniciando descarga del archivo")
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    
    try:
        # Espera hasta que el elemento de descarga esté presente y clickea
        download_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[2]/article/div/div[2]/div/div/div[2]/div/div/div[2]/ul/li[3]/a'))
        )
        download_element.click()
        time.sleep(10)  # Espera para asegurarse de que la descarga se inicie
        logging.info("Descarga del archivo completada")
        show_notification("Descarga Completada", "El archivo IMS ha sido descargado.")
    except Exception as e:
        logging.error(f"Error durante la descarga del archivo: {e}")
    finally:
        driver.quit()

# Función principal que se ejecuta cada 28 días
def main():
    while True:
        today = datetime.now()
        if today.day == 5:
            logging.info("Es el día 5 del mes, comenzando chequeo")
            while True:
                if check_page_with_selenium(link, search_text):
                    open_browser_and_download(link)
                    break
                time.sleep(check_interval)  # Espera 1 hora antes de volver a comprobar
        else:
            logging.info("No es el día 5 del mes, esperando 1 día")
        time.sleep(86400)  # Espera un día antes de volver a comprobar

if __name__ == "__main__":
    logging.info("Iniciando el script de automatización")
    main()
