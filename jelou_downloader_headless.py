#!/usr/bin/env python3
"""
Jelou Downloader (Headless) - Compatible con GitHub Actions
Descarga datos de bases de datos de Jelou.ai usando requests
"""
import sys
import json
import logging
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
    from openpyxl import load_workbook
    import pandas as pd
except ImportError:
    print("Instalando dependencias...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "openpyxl", "pandas", "-q"])
    import requests
    from openpyxl import load_workbook
    import pandas as pd

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
TEMP_DIR = SCRIPT_DIR / 'downloads_temp'

# Mapeo de bases de datos a archivos Excel
DATABASES = {
    5352: {
        'name': 'Casos PMA Tech Support',
        'file': 'Canal Chat.xlsx',
        'sheet': 'Chat'
    },
    5372: {
        'name': 'Casos ticketera tech support',
        'file': 'Canal Correo.xlsx',
        'sheet': 'Correo'
    },
    6129: {
        'name': 'Consultas entrantes',
        'file': 'Chats AI Agent.xlsx',
        'sheet': 'IA'
    },
    6264: {
        'name': 'NPS bot self service',
        'file': 'CSAT AI Agent.xlsx',
        'sheet': 'CSAT'
    },
    567: {
        'name': 'Reporte NPS jelou Chatbots',
        'file': 'CSAT Operadores.xlsx',
        'sheet': 'NPS'
    }
}

class JelouDownloaderHeadless:
    def __init__(self, config_path=CONFIG_FILE):
        self.config = self._load_config(config_path)
        self.base_url = self.config['jelou']['base_url']
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def _load_config(self, path):
        if not path.exists():
            logger.error(f"❌ Archivo de configuración no encontrado: {path}")
            sys.exit(1)
        with open(path) as f:
            return json.load(f)

    def download_database(self, db_id):
        """Descarga una base de datos de Jelou"""
        info = DATABASES[db_id]
        logger.info(f"📥 Descargando: {info['name']} (ID: {db_id})")

        try:
            # URL de descarga de la base de datos
            url = f"{self.base_url}/{db_id}"

            # Intentar descargar con diferentes formatos/métodos
            # Primero intentamos exportar como CSV/Excel si hay un endpoint de exportación
            export_url = f"{url}/export"

            headers = {
                'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, text/csv'
            }

            logger.info(f"  🔗 Intentando descargar desde: {export_url}")

            response = self.session.get(export_url, headers=headers, timeout=30)

            if response.status_code == 200:
                # Guardar el archivo descargado
                temp_file = TEMP_DIR / f"temp_{db_id}.xlsx"
                with open(temp_file, 'wb') as f:
                    f.write(response.content)

                logger.info(f"  ✅ {info['name']} descargado ({len(response.content)} bytes)")
                return temp_file
            else:
                logger.warning(f"  ⚠️ Status {response.status_code} para {info['name']}")
                return None

        except Exception as e:
            logger.error(f"  ❌ Error descargando {info['name']}: {e}")
            return None

    def process_downloads(self):
        """Procesa los archivos descargados"""
        logger.info("")
        logger.info("📊 Procesando descargas...")

        # Crear directorio temporal si no existe
        TEMP_DIR.mkdir(exist_ok=True)

        results = {}

        for db_id, info in DATABASES.items():
            logger.info(f"{'─' * 70}")
            logger.info(f"📋 {info['name']}")
            logger.info(f"{'─' * 70}")

            temp_file = self.download_database(db_id)

            if temp_file and temp_file.exists():
                try:
                    # Copiar el archivo al destino final
                    dest_file = SCRIPT_DIR / info['file']

                    # Leer el archivo temporal
                    df = pd.read_excel(temp_file, sheet_name=0)

                    # Guardar en el archivo final
                    with pd.ExcelWriter(dest_file, engine='openpyxl') as writer:
                        df.to_excel(writer, sheet_name=info['sheet'], index=False)

                    # Limpiar temp
                    temp_file.unlink()

                    logger.info(f"  ✅ {info['file']} actualizado ({len(df)} filas)")
                    results[info['file']] = True

                except Exception as e:
                    logger.error(f"  ❌ Error procesando {info['file']}: {e}")
                    results[info['file']] = False
            else:
                logger.error(f"  ❌ No se pudo descargar {info['name']}")
                results[info['file']] = False

            time.sleep(1)  # Pequeña pausa entre descargas

        return results

    def run(self):
        """Ejecuta el proceso de descarga"""
        logger.info("=" * 70)
        logger.info("🤖 Jelou Downloader (Headless) - Compatible GitHub Actions")
        logger.info(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)

        results = self.process_downloads()

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

def main():
    downloader = JelouDownloaderHeadless()
    success = downloader.run()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
