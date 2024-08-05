# Automatización de Descarga de IMS e IPC del INE

Este proyecto automatiza la descarga del archivo IMS e IPC del Instituto Nacional de Estadística de Uruguay. El script verifica si el archivo está disponible el 5 de cada mes, y si lo está, lo descarga automáticamente.

## Requisitos

- Python 3.x
- Google Chrome
- ChromeDriver compatible con la versión de Google Chrome instalada (en mi caso 127)

## Instalación de Dependencias

1. **Instalar Python**:
   - Descarga e instala Python desde [python.org](https://www.python.org/).

2. **Instalar Selenium**:
   - Abre una terminal y ejecuta:
     ```sh
     pip install selenium
     ```

3. **Descargar ChromeDriver**:
   - Ve a [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) y descarga la versión compatible con tu versión de Chrome.
   - Extrae el archivo descargado y coloca `chromedriver.exe` en una ubicación accesible, por ejemplo: `C:\chromedriver.exe`.

## Configuración del Script

1. **Crear el Script de Automatización**:
   - Crea un archivo llamado `automatizacion_descarga_IMS.py`
   - Crea un archivo llamado `automatizacion_descarga_IPC.py`