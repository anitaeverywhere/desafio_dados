
import requests
from typing import List, Dict, Any, Optional

def fetch_data(url: str) -> Optional[List[Dict[str, Any]]]:
    print(f"Buscando dados da API em: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Dados recebidos com sucesso.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se comunicar com a API: {e}")
        return None