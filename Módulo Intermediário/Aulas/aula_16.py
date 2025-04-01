# Função lambda em python 
# a função lambda é uma função como qualquer outra
# em python. Porém, são funções anônimas que contém apenas uma linha. 
# Ou seja, tudo deve ser contido dentro de uma unica expressão.

# lista = [
#     {'nome': 'Ana', 'sobrenome' : 'moraes'},
#     {'nome': 'maria', 'sobrenome' : 'oliveira'},
#     {'nome': 'amelie', 'sobrenome' : 'silva'},
#     {'nome': 'marta', 'sobrenome' : 'moreira'},
#     {'nome': 'daniel', 'sobrenome' : 'souza'},
# ]

# lista = [ 2,7,4,2,4,7,8]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {'nome': 'Ana', 'sobrenome' : 'moraes'},
    {'nome': 'Maria', 'sobrenome' : 'oliveira'},
    {'nome': 'Amelie', 'sobrenome' : 'silva'},
    {'nome': 'Marta', 'sobrenome' : 'moreira'},
    {'nome': 'Daniel', 'sobrenome' : 'souza'},
]

def ordena(item):
    return item['nome']


lista.sort(key=ordena)

for item in lista:
    print(item)