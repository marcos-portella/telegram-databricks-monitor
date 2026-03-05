import os
import requests
import re
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TARGET_URL = "https://www.databricks.com/dataaisummit/agenda"
DB_FILE = "last_count.txt"

def get_last_count():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding='utf-8') as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
    return 0

def save_current_count(count):
    with open(DB_FILE, "w", encoding='utf-8') as f:
        f.write(str(count))

def check_databricks_sessions():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(TARGET_URL, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')

        results_element = soup.find(string=re.compile(r'Results\s*\(\d+\)'))
        
        if results_element:
            match = re.search(r'\((\d+)\)', str(results_element))
            if match:
                return int(match.group(1))
        
        print("Aviso: Valor não encontrado no HTML. Mantendo contagem anterior.")
        return get_last_count()
        
    except Exception as e:
        print(f"Erro na extração: {e}")
        return get_last_count()

def send_notification(count):
    message = f"🚨 **Novo Alerta Noach!**\nO número de sessões no Databricks Summit aumentou para: **{count}**\n\nConfira em: {TARGET_URL}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    print(f"Resposta do Telegram: {response.status_code}")

last_known = get_last_count()
current = check_databricks_sessions()

if current > last_known:
    send_notification(current)
    save_current_count(current)
    print(f"Sucesso: Notificação enviada! De {last_known} para {current}")
else:
    print(f"Sem novidades: {current} sessões (anterior era {last_known})")
