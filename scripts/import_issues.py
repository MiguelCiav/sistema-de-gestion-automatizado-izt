#!/usr/bin/env python3
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error

# Configuración del repositorio
REPO_OWNER = "MiguelCiav"
REPO_NAME = "sistema-de-gestion-automatizado-izt"
STORIES_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "HISTORIAS_DE_USUARIO_DETALLADAS.md")

def parse_stories(filepath):
    if not os.path.exists(filepath):
        print(f"[-] Error: No se encontró el archivo de historias en {filepath}")
        return []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stories = []
    # Buscar secciones de HU
    pattern = re.compile(r'^(### HU\d+\s*-\s*[^\n]+)', re.MULTILINE)
    parts = pattern.split(content)
    
    for i in range(1, len(parts), 2):
        title = parts[i].replace('###', '').strip()
        body = parts[i+1].strip()
        stories.append({
            'title': title,
            'body': body
        })
    return stories

def create_issue(token, title, body):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Python-Issue-Importer"
    }
    
    # Asignar etiquetas básicas
    labels = ["user-story"]
    
    # Mapeo de MVPs
    mvp_codes = ["HU01", "HU02", "HU03", "HU04", "HU05", "HU06", "HU07", "HU08", "HU09", "HU10"]
    if any(code in title for code in mvp_codes):
        labels.append("MVP")
        labels.append("prioridad-alta")
    elif "HU17" in title:
        labels.append("prioridad-media")
    else:
        labels.append("fase-2")
        labels.append("prioridad-baja")
        
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get('html_url'), res_data.get('number')
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        try:
            err_json = json.loads(error_msg)
            message = err_json.get('message', error_msg)
        except:
            message = error_msg
        print(f"[-] Error al crear '{title}': HTTP {e.code} - {message}")
        return None, None
    except Exception as e:
        print(f"[-] Error inesperado al crear '{title}': {str(e)}")
        return None, None

def main():
    print("="*60)
    print("  Importador Automatizado de Historias de Usuario a GitHub Issues")
    print("="*60)
    
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[-] Error: La variable de ambiente GITHUB_TOKEN no está definida.")
        print("\nPara ejecutar este script:")
        print("1. Genera un Personal Access Token (Classic o Fine-grained) en GitHub")
        print(f"   con permisos de escritura (Read & Write) para 'Issues' en {REPO_OWNER}/{REPO_NAME}.")
        print("2. Ejecuta el script exportando tu token:")
        print("   export GITHUB_TOKEN=\"tu_token_aqui\"")
        print("   python3 scripts/import_issues.py")
        sys.exit(1)
        
    print("[+] Cargando historias de usuario desde el archivo...")
    stories = parse_stories(STORIES_FILE)
    if not stories:
        print("[-] No se encontraron historias para importar.")
        sys.exit(1)
        
    print(f"[+] Se detectaron {len(stories)} historias de usuario.")
    print(f"[+] Iniciando importación en el repositorio: {REPO_OWNER}/{REPO_NAME}")
    print("-" * 60)
    
    created_count = 0
    for idx, story in enumerate(stories, 1):
        title = story['title']
        body = story['body']
        
        print(f"[{idx}/{len(stories)}] Importando: {title}...", end="", flush=True)
        url, num = create_issue(token, title, body)
        if url:
            print(f" OK (Issue #{num})")
            created_count += 1
            # Evitar el rate limiting preventivamente
            time.sleep(1)
        else:
            print(" FALLÓ")
            
    print("-" * 60)
    print(f"[+] Proceso completado. Se crearon {created_count} de {len(stories)} issues con éxito.")
    print("="*60)

if __name__ == "__main__":
    main()
