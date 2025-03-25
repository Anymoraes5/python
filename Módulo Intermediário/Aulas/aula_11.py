'''
Metodos úteis dos dicionarios em python 
len - quantas chaves
keys - iteravel com a chaves
values - iteravel com os valores
set de faut - add valor se a chave não existe 
copy retorna uma copia rasa(shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada(del)
poitem - apaga o ultimo item adicionado 
update - atualiza um dicionario com outro 
'''
pessoa = {
    'nome' : 'Ana Caroline',
    'sobrenome' : 'Moraes',
    'sobrenome' : 'Moraes1',
    'sobrenome' : 'Moraes2', #2 chaves apenas pois repetiu a chave sobrenome
    'idade' : 900
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

#print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave , valor)

# for valor in pessoa.values():
#     print(valor)

# for chave in pessoa:
#     print(chave)

