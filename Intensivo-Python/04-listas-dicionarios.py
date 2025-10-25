from typing import Dict, Any

# Aula 4: Type Hint, Listas e Dicionários 

# Type Hint: ajuda a tornar o código mais legóvel e seguro, especificando o tipo do dado por funções e variáveis.

# Sem Type Hint: 
idade = 30
altura = 1.60
nome = 'Maria'
is_estudante = True 

# Com Type Hint
idade: int = 30
altura: float = 1.60
nome: str = 'Maria'
is_estudante: bool = True

# Tipagem 
# Tipagem Estática: o tipo de variável precisa ser declarado explicitamente no momento da compilação.
# Tipagem Dinamica: os tipos são inferidos da variavel, se ela é int ou string por exemplo. 


# Listas e Dicionários: São super importantes para engenharia de dados 

# Listas 
produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "tenis"

produtos:list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() #tira o ultimo produto que entrou
produtos.remove() # tira o produto

print(produtos)
 
# Dicionários: É tipo uma lista que consigo atribuir uma chave valor, uma referencia do que será cada chave.

lista = ["Sapato", 39, 10.38, True]

dicionario: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preço": 10.38,
    "disponibilidade": True
}

# EXEMPLO: Crie um dicionário para armazenar informações de um livro, incluindo titulo, autor e ano de publicação; Imprima cada informação.

from typing import Dict, Any

livro: Dict[str, Any] = {
    "titulo":"Ensaio sobre a Cegueira",
    "autor": "Jose Saramago",
    "ano": "1980"
}

lista_elementos: list = livro.items()
for elemento in lista_elementos:
    print(elemento)
     
