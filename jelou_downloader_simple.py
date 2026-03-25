#!/usr/bin/env python3
"""
Jelou Downloader Simple - Verifica que los archivos existan
Para usar en GitHub Actions cuando los archivos ya están descargados
"""
import sys
import logging
from pathlib import Path
from datetime import datetime

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

# Archivos Excel esperados
EXCEL_FILES = [
    "Canal Chat.xlsx",
    "Canal Correo.xlsx",
    "Chats AI Agent.xlsx",
    "CSAT AI Agent.xlsx",
    "CSAT Operadores.xlsx"
]

def main():
    logger.info("=" * 70)
    logger.info("🤖 Jelou Downloader Simple - Verificando archivos")
    logger.info(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 70)
    logger.info("")

    all_exist = True
    logger.info("📊 Verificando archivos Excel:")
    logger.info("─" * 70)

    for file_name in EXCEL_FILES:
        file_path = SCRIPT_DIR / file_name
        if file_path.exists():
            size = file_path.stat().st_size / 1024  # KB
            logger.info(f"✅ {file_name:<30} ({size:.1f} KB)")
        else:
            logger.warning(f"⚠️ {file_name:<30} NO ENCONTRADO")
            all_exist = False

    logger.info("─" * 70)
    logger.info("")

    if all_exist:
        logger.info("✅ ¡TODOS LOS ARCHIVOS EXISTEN!")
        logger.info("")
        logger.info("Los archivos están listos para ser actualizados en GitHub.")
        logger.info("El workflow hará commit de cualquier cambio encontrado.")
        logger.info("")
        return 0
    else:
        logger.warning("⚠️ Algunos archivos no fueron encontrados")
        logger.warning("")
        logger.warning("Por favor:")
        logger.warning("1. Abre https://apps.jelou.ai/datum/databases/")
        logger.warning("2. Descarga cada base de datos manualmente")
        logger.warning("3. Coloca los archivos en esta carpeta")
        logger.warning("4. Haz commit y push")
        logger.warning("")
        return 0  # No fallar, solo advertir

if __name__ == '__main__':
    sys.exit(main())
