# src/transformar.py
# -----------------------------------
# ETAPA 2: TRANSFORMAÇÃO
# Limpa e padroniza os dados extraídos
# -----------------------------------

def transformar_dados(dados):
    
    dados_transformados = []

    for registro in dados:
        # Tratamento de ano
        try:
            registro['ano'] = int(registro['ano'])
        except:
            registro['ano'] = 0  # valor padrão se não for possível converter

        # Tratamento de nota
        try:
            registro['nota'] = float(registro['nota'])
        except:
            registro['nota'] = 0.0  # valor padrão

        # Padronização de strings
        registro['titulo'] = registro['titulo'].strip().title() if registro['titulo'] else "Desconhecido"
        registro['genero'] = registro['genero'].strip().title() if registro['genero'] else "Desconhecido"

        dados_transformados.append(registro)

    print(f"[INFO] Transformação concluída. {len(dados_transformados)} registros processados.")
    return dados_transformados


if __name__ == "__main__":
    # Exemplo
    dados_exemplo = [
        {'titulo': 'matrix', 'ano': '1999', 'nota': '8.7', 'genero': 'Ficção Científica'},
        {'titulo': 'titanic ', 'ano': '', 'nota': '7.8', 'genero': 'romance'}
    ]

    dados_limpos = transformar_dados(dados_exemplo)
    for registro in dados_limpos:
        print(registro)
