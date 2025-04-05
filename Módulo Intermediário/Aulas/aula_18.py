#print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)


lista = [
    numero*2
    for numero in range(10)
]
print(list(range(10)))
print(lista)

# Mapeamento de dados em list compreheinsion
produtos = [
    {'nome' : 'p1', 'preco' : 20, },
    {'nome' : 'p2', 'preco' : 10, },
    {'nome' : 'p3', 'preco' : 30, },
]
novos_produtos = [
    {**produto, 'preco' : produto['preco'] * 1.05}
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')