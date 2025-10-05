# Aula 02 - TypeError, Type Check, Type Conversion, try-except e if

try: 
    numero_01 = int(input('Inserir um numero inteiro: '))
    numero_02 = int(input('Inserir um numero inteiro: '))
    resultado = numero_01 // numero_02
    print(resultado)
except ZeroDivisionError:   # Sempre pensar nos tipos de erro que tem no Python
    print('Divisão por inteiro ou por zero.')
    
#Exemplo que causa TypeError:
try:
    #resultado = len('Maria')
    resultado = len(5)
    print(resultado)
except TypeError as e:
    print(e) # Imprime mensagem de erro
else: 
    print('Tudo ocorreu bem')
    
#Isintance = Ele analisa primeiro se algo é do tipo declarado, compara com o tipo que queremos 
numero = 10
if isinstance(int,numero):
    print("A variavel é um inteiro.")
else: 
    print('A variavel não é um inteiro.')


# DESAFIO

# Cálculo do KPI do bonus de 2024 é de '1000+salario*bonus' do usuario 

# 1) Nome do usuário
nome_usuario = input('Insira o nome do usuário aqui:')
if nome_usuario.isdigit():
    print(nome_usuario.isdigit())
elif len(nome_usuario) == 0:
    print("Voce não digitou o nome correto do usuário.")
elif nome_usuario.isspace():
    print('Voce digitou só espaço.')
    
# 2) Valor do salário: 
salario_usuario = float(input("Digite o salário do usuário:"))
if isinstance(salario_usuario, float):
    print('A variável é um número flutuante.')
else:
    print('A variável não é um número flutuante.')

# 3) Valor do bonus: 
salario_bonus = float(input("Digite o bonus do usuário:"))
if isinstance(salario_bonus, float):
    print('A variável é um número flutuante.')
else:
    print('A variável não é um número flutuante.')