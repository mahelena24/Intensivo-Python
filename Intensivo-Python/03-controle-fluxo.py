# Aula 03 - Controle de Fluxo: DEBUG, IF, FOR, While, Listas e Dicionários


# Primeiro controle de fluxo: IF
x = int(input("Inserir um inteiro: "))

if x<0:
    x=0
    print("Negativo mudado para zero.")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else:
    print("More")
    
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

leitura = int(input("Digite a leitura realizada:"))

if leitura<18:
    print("Temperatura Baixa")
elif 18 <= leitura <= 26:
    print("Temperatura Normal") 
elif leitura > 26:
    print("Temperatura Alta")
    

# Segundo controle de fluxo: FOR
# O FOR é quando tenho uma condição CONHECIDA de onde eu quero parar
# Ele para no ultimo valor, não itenra o último valor
for i in range(1,5):
    print(i)


lista = ['Maria', 'Mariana']
for aluno in lista:
    print(aluno)

# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)

# Terceiro controle de fluxo: WHILE
# O while usamos quando temos uma condição DESCONHECIDA de quando iremos parar

import time

condicao = True

while condicao:
    print("Execcute a minha ETL")
    time.sleep(5)
    
# DESAFIO:
nome_usuario = False
salario_usuario = False
salario_bonus = False


# 1) Nome do usuário
while nome_usuario is not True:
    nome_usuario = input('Insira o nome do usuário aqui:')
    if nome_usuario.isdigit():
        print(nome_usuario.isdigit())
    elif len(nome_usuario) == 0:
        print("Voce não digitou o nome correto do usuário.")
    elif nome_usuario.isspace():
        print('Voce digitou só espaço.')
    else:
        nome_usuario = True
        print("Nome válido:", nome_usuario)
    
# 2) Valor do salário: 
while salario_usuario is not True:
    salario_usuario = float(input("Digite o salário do usuário:"))
    if isinstance(salario_usuario, float):
        print('A variável é um número flutuante.')
    elif ValueError:
        print('A variável não é um número flutuante.')
    else:
        salario_usuario = True
        print("Salário válido:", salario_usuario)

    # 3) Valor do bonus: 
while salario_bonus is not True:
    salario_bonus = float(input("Digite o bonus do usuário:"))
    if isinstance(salario_bonus, float):
        print('A variável é um número flutuante.')
    elif ValueError:
        print('A variável não é um número flutuante.')
    else:
        salario_bonus = True
        print("Bonus válido:", salario_bonus)

bonus_recebido = 1000 + salario_usuario * salario_bonus 
print(f"{nome_usuario}, seu salário é R${salario_usuario:.2F} e o bonus final é de R${bonus_recebido:.2f}")