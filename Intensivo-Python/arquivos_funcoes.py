# Aula 05: Arquivos e funções 
# Utilizando aqui o próprio módulo de CSV do Python, mas tem outros métodos, como o próprio Pandas 

import csv 

# Caminho para o CSV 
caminho_arquivo = '/Users/mariahelenamartins/Documents/Jornada de Dados/Intensivo-Python/exemplo.csv'

#Inicializa uma lista vazia para armazenar os dados 
dados = []

# Usa o gerenciador de contexto 'with' para abrir o arquivo 
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    #Cria um objeto leitor de CSV:
    leitor_csv = csv.DictReader(arquivo)
    
    #Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        dados.append(linha)
        
        
#Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)


# Funções 
lista_numeros: list = [40, 60, 70, 1000, 560]

# Input -> Função -> Output
def ordernar_lista_numeros(numeros:list) -> list:
    nova_lista_numeros = lista_numeros.copy()
    
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]
    
    return nova_lista_numeros

nova_lista = ordernar_lista_numeros(lista_numeros)
print(nova_lista)
        