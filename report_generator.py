

import csv
from typing import List, Dict, Any

def generate_console_report(stats: Dict[str, Any], user_id: int):
   
    print("\n--- Relatório de Estatísticas ---")
    print(f"Análise para o usuário de ID: {user_id}")
    
    print(f"Total de posts: {stats['total_posts']}") 
    
    print(f"Tamanho médio do corpo dos posts: {stats['avg_body_length']:.2f} caracteres") # [cite: 33]
    
    print("\nTop 3 palavras mais frequentes nos títulos:") 
    for word, count in stats['top_words']:
        print(f"- {word} ({count} vezes)") 

def generate_csv_report(posts: List[Dict[str, Any]], filename: str):
    if not posts:
        print("\nNenhum dado para gerar o relatório CSV.")
        return

    print(f"\nGerando arquivo CSV: {filename}...")
    
    
    header = ["id", "userId", "title", "body_length"] 

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            
           
            writer.writeheader()
            
            
            for post in posts:
            
                row = {
                    'id': post.get('id'),
                    'userId': post.get('userId'),
                    'title': post.get('title'),
                    'body_length': len(post.get('body', ''))
                }
                writer.writerow(row)
        print(f"Arquivo '{filename}' gerado com sucesso.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo '{filename}': {e}")