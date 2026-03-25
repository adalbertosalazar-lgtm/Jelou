#!/usr/bin/env python3
"""
Jelou Downloader Automático - Selenium Headless
Descarga datos automáticamente de Jelou.ai sin intervención
Compatible con GitHub Actions
"""
import sys
import json
import logging
import time
import os
from pathlib import Path
from datetime import datetime

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("Instalando Selenium...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "-q"])
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jelou_downloader.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / 'config.json'
DOWNLOADS_DIR = SCRIPT_DIR / 'downloads_auto'

DATABASES = {
    5352: {'name': 'Casos PMA Tech Support', 'file': 'Canal Chat.xlsx'},
    5372: {'name': 'Casos ticketera tech support', 'file': 'Canal Correo.xlsx'},
    6129: {'name': 'Consultas entrantes', 'file': 'Chats AI Agent.xlsx'},
    6264: {'name': 'NPS bot self service', 'file': 'CSAT AI Agent.xlsx'},
    567: {'name': 'Reporte NPS jelou Chatbots', 'file': 'CSAT Operadores.xlsx'},
}

class JelouDownloaderAuto:
    def __init__(self, config_path=CONFIG_FILE):
        self.config = self._load_config(config_path)
        self.base_url = self.config['jelou']['base_url']
        self.driver = None

    def _load_config(self, path):
        if not path.exists():
            logger.error(f"❌ Archivo de configuración no encontrado: {path}")
            sys.exit(1)
        with open(path) as f:
            return json.load(f)

    def setup_driver(self):
        """Configura el navegador Chrome headless"""
        logger.info("🔧 Configurando navegador Chrome headless...")

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')

        # Configurar descargas
        DOWNLOADS_DIR.mkdir(exist_ok=True)
        prefs = {'download.default_directory': str(DOWNLOADS_DIR)}
        chrome_options.add_experimental_option('prefs', prefs)

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            logger.info("✅ Navegador configurado correctamente")
            return True
        except Exception as e:
            logger.error(f"❌ Error configurando navegador: {e}")
            logger.info("⚠️ Nota: GitHub Actions necesita Chrome/Chromium instalado")
            return False

    def download_database(self, db_id):
        """Descarga una base de datos"""
        info = DATABASES[db_id]
        logger.info(f"📥 Descargando: {info['name']} (ID: {db_id})")

        try:
            url = f"{self.base_url}/{db_id}"
            self.driver.get(url)

            # Esperar a que cargue la página
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            time.sleep(2)  # Esperar a que cargue completamente

            # Buscar el botón de descarga
            try:
                download_btn = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Download')] | //button[contains(., 'Download')]")
                download_btn.click()
                logger.info(f"  ✅ {info['name']} - Descarga iniciada")
                time.sleep(3)  # Esperar a que descargue
                return True
            except:
                logger.warning(f"  ⚠️ No se encontró botón de descarga para {info['name']}")
                return False

        except Exception as e:
            logger.error(f"  ❌ Error descargando {info['name']}: {e}")
            return False

    def move_downloads(self):
        """Mueve los archivos descargados a la ubicación final"""
        logger.info("")
        logger.info("📁 Moviendo archivos descargados...")

        results = {}
        for db_id, info in DATABASES.items():
            filename = info['file']

            # Buscar el archivo descargado
            temp_files = list(DOWNLOADS_DIR.glob(f"{filename}*"))

            if temp_files:
                temp_file = temp_files[0]
                dest_file = SCRIPT_DIR / filename

                # Mover archivo
                temp_file.rename(dest_file)
                size = dest_file.stat().st_size / 1024
                logger.info(f"✅ {filename:<30} ({size:.1f} KB)")
                results[filename] = True
            else:
                logger.warning(f"⚠️ {filename:<30} NO ENCONTRADO")
                results[filename] = False

        return results

    def run(self):
        """Ejecuta la descarga"""
        logger.info("=" * 70)
        logger.info("🤖 Jelou Downloader Automático (Selenium Headless)")
        logger.info(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)
        logger.info("")

        # Setup navegador
        if not self.setup_driver():
            logger.error("❌ No se pudo configurar el navegador")
            return False

        try:
            # Descargar cada base de datos
            for db_id in DATABASES.keys():
                self.download_database(db_id)
                logger.info("")

            # Mover descargas
            results = self.move_downloads()

            # Resumen
            logger.info("")
            logger.info("=" * 70)
            logger.info("📊 RESUMEN DE DESCARGAS")
            logger.info("=" * 70)

            all_success = True
            for file_name, success in results.items():
                status = "✅" if success else "❌"
                logger.info(f"{status} {file_name}")
                if not success:
                    all_success = False

            logger.info("=" * 70)
            if all_success:
                logger.info("✅ ¡TODAS LAS DESCARGAS COMPLETADAS!")
            else:
                logger.warning("⚠️ Algunas descargas fallaron")

            logger.info(f"⏰ Finalizado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info("=" * 70)

            return all_success

        finally:
            if self.driver:
                self.driver.quit()
                logger.info("🔌 Navegador cerrado")

def main():
    downloader = JelouDownloaderAuto()
    success = downloader.run()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
