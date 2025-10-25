import csv

def carregar_dados(dados, caminho_arquivo_saida):

    if not dados:
        print("[AVISO] Nenhum dado para salvar.")
        return

    # Pega as chaves do primeiro registro como cabeçalho
    cabecalho = dados[0].keys()

    try:
        with open(caminho_arquivo_saida, mode='w', encoding='utf-8', newline='') as arquivo_csv:
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
            escritor_csv.writeheader()  # escreve o cabeçalho
            for registro in dados:
                escritor_csv.writerow(registro)
        print(f"[INFO] Carga concluída. Arquivo salvo em: {caminho_arquivo_saida}")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema ao salvar o arquivo: {e}")


if __name__ == "__main__":
    dados_exemplo = [
        {'titulo': 'Matrix', 'ano': 1999, 'nota': 8.7, 'genero': 'Ficção Científica'},
        {'titulo': 'Titanic', 'ano': 1997, 'nota': 7.8, 'genero': 'Romance'}
    ]

    caminho_saida = "/Users/mariahelenamartins/Documents/Jornada de Dados/Pipeline Filmes /dados/filmes_limpos.csv"
    carregar_dados(dados_exemplo, caminho_saida)