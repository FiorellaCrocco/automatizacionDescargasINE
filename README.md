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

2. **Agregar Tarea Programada en Windows**:
   - **Abrir el Programador de Tareas**:
     - Presiona `Win + R`, escribe `taskschd.msc` y presiona `Enter`.
   - **Crear una Nueva Tarea**:
     - En el Programador de Tareas, haz clic en `Crear Tarea Básica` en el panel derecho.
   - **Configurar la Tarea**:
     - **General**:
       - En la pestaña `General`, dale un nombre a la tarea, por ejemplo, `DescargaAutomaticaIMS`.
       - Opcional: Añade una descripción.
     - **Desencadenadores**:
       - Ve a la pestaña `Desencadenadores` y selecciona `Mensualmente` 
       - Ajusta el día y la hora de inicio a las 09:00 o a la hora que prefieras.
       - Asegúrate de que la tarea se repita cada día 5 de todos los meses.
     - **Acciones**:
       - Ve a la pestaña `Acciones` seleccionamos `Iniciar un programa`.
       - En `Programa/Script`, navega y selecciona el ejecutable de Python (por ejemplo, `C:\Python39\python.exe`).
       - En `Agregar argumentos`, escribe la ruta completa a tu script, por ejemplo:
         ```sh
         "C:\..\Documents\automatizacion_descarga_IMS.py"
         ```
     - **Condiciones**:
       - Ve a la pestaña `Condiciones` y desmarca `Iniciar la tarea solo si el equipo está en corriente alterna`.
   - **Guardar la Tarea**:
     - Haz clic en `Aceptar` para guardar la tarea.
