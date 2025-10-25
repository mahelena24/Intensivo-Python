from typing import Dict, Any

livro: Dict[str, Any] = {
    "titulo":"Ensaio sobre a Cegueira",
    "autor": "Jose Saramago",
    "ano": "1980"
}

lista_elementos: list = livro.items()
for elemento in lista_elementos:
    print(elemento)
     