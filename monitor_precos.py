import os
import requests
import pandas as pd
from datetime import datetime

def executar_robo_monitor():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando o robô monitor de preços...")

    url_alvo = "https://fakestoreapi.com/products"
    produtos_brutos = None
    
    try:
        # Tentativa de conexão com o servidor remoto
        resposta = requests.get(url_alvo, timeout=10)
        resposta.raise_for_status() 
        
        # Tenta decodificar o JSON. Se falhar, vai direto para o bloco except genérico
        produtos_brutos = resposta.json()
        print(f"// Conexão de nuvem bem-sucedida! {len(produtos_brutos)} produtos importados.")
        
    except Exception as erro:
        # ESTRATÉGIA DE CONTINGÊNCIA: Se o servidor cair/falhar, usamos dados locais de backup
        print(f"[AVISO] Servidor remoto instável ou inacessível. Ativando banco de dados de contingência local...")
        
        produtos_brutos = [
            {"id": 1, "title": "Monitor Gamer IPS 24p", "price": 149.99, "category": "electronics"},
            {"id": 2, "title": "Teclado Mecânico RGB", "price": 59.99, "category": "electronics"},
            {"id": 3, "title": "SSD M.2 NVMe 1TB Premium", "price": 89.99, "category": "electronics"},
            {"id": 4, "title": "Notebook Corporativo i7 vPro", "price": 1199.00, "category": "electronics"},
            {"id": 5, "title": "Smartphone Processamento IA", "price": 699.99, "category": "electronics"},
            {"id": 6, "title": "Cadeira de Escritório Ergonômica", "price": 120.00, "category": "furniture"}
        ]

    # PASSO 2: Tratamento de Dados (Data Engineering)
    dados_processados = []

    for item in produtos_brutos:
        id_produto = item.get("id")
        nome_produto = item.get("title")
        preco = item.get("price")
        categoria = item.get("category")
        
        produto_formatado = {
            "ID": id_produto,
            "Produto": nome_produto,
            "Preço Original ($)": preco,
            "Preço Convertido (R$)": round(preco * 5.40, 2), 
            "Categoria": categoria,
            "Data da Coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        dados_processados.append(produto_formatado)

    # PASSO 3: Manipulação e Filtros Analíticos (Pandas)
    df = pd.DataFrame(dados_processados)

    # Regra de negócio: Filtrar eletrônicos com valor convertido acima de R$ 300
    eletronicos_premium = df[(df["Categoria"] == "electronics") & (df["Preço Convertido (R$)"] > 300)]

    # PASSO 4: Exportação Automatizada
    nome_arquivo = "relatorio_precos_concorrentes.xlsx"
    eletronicos_premium.to_excel(nome_arquivo, index=False)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Processo finalizado!")
    print(f"// Relatório gerado com sucesso: {os.path.abspath(nome_arquivo)}")
    print(f"// Registros exportados para análise do cliente: {len(eletronicos_premium)}")

if __name__ == "__main__":
    executar_robo_monitor()
