# Nessa primeira etapa do nosso ETL, iremos realizar a extração das nossas informações do CSV e salvar em uma lista de dicionários, que será mais fácil de manipular.

import csv 

# Caminho do CSV 
filmes = '/Users/mariahelenamartins/Documents/Jornada de Dados/Pipeline Filmes /dados/filmes.csv'
dados = []

def extrair_dados(caminho_arquivo):
    
    try:
            with open(filmes, mode='r', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    dados.append(linha)
            print(f"[INFO] Extração concluída. {len(dados)} registros lidos.")
    except FileNotFoundError:
            print(f"[ERRO] Arquivo não encontrado: {filmes}")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema ao ler o arquivo: {e}")
        
    return dados


if __name__ == "__main__":
    caminho = "../dados/filmes.csv"  # ajuste conforme sua estrutura de pastas
    dados_extraidos = extrair_dados(filmes)
    
    # Mostra os 5 primeiros registros
    for registro in dados_extraidos[:5]:
        print(registro)