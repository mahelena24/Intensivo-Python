from extrair import extrair_dados
from transformar import transformar_dados
from carregar import carregar_dados

if __name__ == "__main__":
    caminho_entrada = "/Users/mariahelenamartins/Documents/Jornada de Dados/Pipeline Filmes /dados/filmes.csv"
    caminho_saida = "/Users/mariahelenamartins/Documents/Jornada de Dados/Pipeline Filmes /dados/filmes_limpos.csv"

    # 1️⃣ Extração
    dados_extraidos = extrair_dados(caminho_entrada)

    # 2️⃣ Transformação
    dados_limpos = transformar_dados(dados_extraidos)

    # 3️⃣ Carga
    carregar_dados(dados_limpos, caminho_saida)