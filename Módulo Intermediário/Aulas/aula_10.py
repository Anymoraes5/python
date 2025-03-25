"""
Dicionários em python (tipo dict)
dicionários são estruturas de dados do tipo 
par de "chave" e "valor".

Chaves podem ser consideradas como o "indice" 
que vimos na lista e podem ser de tipos imutaveis
como; str, int, float, bool, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.
imutaveis: str, int, float, bool, tuple
mutavel: dict , list

pessoa = {
    'nome': 'Ana',
    'sobrenome': 'Moraes',
    'idade': '18'
    'altura': '1.58'
    'endereco': [
    {'rua' : 'tal tal', 'numero': 123},
    {'rua': 'bla bla', 'numero' : 321},
    ]
}
"""

pessoa = {
    'nome': 'Ana', 
    'sobrenome': 'Moraes',
    'idade': '18',
    'altura': '1.58',
    'endereco': [
    {'rua' : 'tal tal', 'numero': 123},
    {'rua': 'bla bla', 'numero' : 321},

    ],
}

print(pessoa, type(pessoa))