#!/usr/bin/env python3
"""
GitHub Uploader - Pushes Excel files to GitHub repository
Updates the Jelou Dashboard with new data by committing files to GitHub
"""
import sys
import json
import logging
import base64
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("Instalando dependencias...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('github_uploader.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / 'config.json'

# Excel files to upload to GitHub
EXCEL_FILES = {
    "Canal Chat.xlsx": "datos/Canal Chat.xlsx",
    "Canal Correo.xlsx": "datos/Canal Correo.xlsx",
    "Chats AI Agent.xlsx": "datos/Chats AI Agent.xlsx",
    "CSAT AI Agent.xlsx": "datos/CSAT AI Agent.xlsx",
    "CSAT Operadores.xlsx": "datos/CSAT Operadores.xlsx"
}

class GitHubUploader:
    def __init__(self, config_path=CONFIG_FILE):
        self.config = self._load_config(config_path)
        self.github_token = self.config.get('github', {}).get('token')
        self.repo = self.config.get('github', {}).get('repo')
        self.base_url = f"https://api.github.com/repos/{self.repo}/contents"

    def _load_config(self, path):
        if not path.exists():
            logger.error(f"❌ Archivo de configuración no encontrado: {path}")
            sys.exit(1)
        with open(path) as f:
            return json.load(f)

    def upload_file(self, local_path, github_path):
        """Sube un archivo a GitHub"""
        logger.info(f"📤 Subiendo: {local_path.name} → {github_path}")

        try:
            # Leer el archivo
            with open(local_path, 'rb') as f:
                file_content = f.read()

            # Codificar en base64
            encoded_content = base64.b64encode(file_content).decode('utf-8')

            # Preparar los headers
            headers = {
                'Authorization': f'token {self.github_token}',
                'Content-Type': 'application/json',
                'Accept': 'application/vnd.github.v3+json'
            }

            # URL del archivo en GitHub
            file_url = f"{self.base_url}/{github_path}"

            # Primero intentamos obtener el archivo existente para tener su SHA
            try:
                response = requests.get(file_url, headers=headers)
                existing_sha = response.json().get('sha') if response.status_code == 200 else None
            except:
                existing_sha = None

            # Preparar el payload
            payload = {
                'message': f'🤖 Actualización automática de datos - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                'content': encoded_content,
                'branch': 'main'
            }

            if existing_sha:
                payload['sha'] = existing_sha

            # Hacer la petición PUT para subir el archivo
            response = requests.put(
                file_url,
                headers=headers,
                json=payload
            )

            if response.status_code in [200, 201]:
                logger.info(f"  ✅ {local_path.name} subido correctamente")
                return True
            else:
                logger.error(f"  ❌ Error al subir {local_path.name}")
                logger.error(f"  Status: {response.status_code}")
                logger.error(f"  Response: {response.text}")
                return False

        except Exception as e:
            logger.error(f"  ❌ Error subiendo {local_path.name}: {e}")
            return False

    def run(self):
        """Ejecuta la carga de archivos a GitHub"""
        logger.info("=" * 70)
        logger.info("🚀 GitHub Uploader - Subiendo archivos Excel")
        logger.info(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)

        # Verificar que tenemos el token
        if not self.github_token:
            logger.error("❌ Token de GitHub no configurado en config.json")
            logger.error("Por favor, agrega 'github' -> 'token' a tu config.json")
            return False

        if not self.repo:
            logger.error("❌ Repositorio de GitHub no configurado en config.json")
            logger.error("Por favor, agrega 'github' -> 'repo' a tu config.json (ej: usuario/repo)")
            return False

        logger.info(f"📦 Repositorio: {self.repo}")
        logger.info(f"🔑 Token: {self.github_token[:20]}...")

        results = {}
        all_success = True

        for local_name, github_path in EXCEL_FILES.items():
            local_path = SCRIPT_DIR / local_name

            if not local_path.exists():
                logger.warning(f"⚠️ Archivo no encontrado: {local_name}")
                results[local_name] = False
                all_success = False
                continue

            logger.info("")
            logger.info(f"{'─' * 70}")
            logger.info(f"📋 {local_name}")
            logger.info(f"{'─' * 70}")

            success = self.upload_file(local_path, github_path)
            results[local_name] = success

            if not success:
                all_success = False

        # Resumen
        logger.info("")
        logger.info("=" * 70)
        logger.info("📊 RESUMEN DE CARGA")
        logger.info("=" * 70)

        for file_name, success in results.items():
            status = "✅" if success else "❌"
            logger.info(f"{status} {file_name}")

        logger.info("=" * 70)
        if all_success:
            logger.info("✅ ¡TODOS LOS ARCHIVOS SUBIDOS CORRECTAMENTE!")
            logger.info("📊 El dashboard se actualizará en breve")
        else:
            logger.warning("⚠️ Algunos archivos no pudieron subirse")
            logger.warning("Revisa el log para más detalles")

        logger.info(f"⏰ Finalizado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)

        return all_success

def main():
    uploader = GitHubUploader()
    success = uploader.run()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
