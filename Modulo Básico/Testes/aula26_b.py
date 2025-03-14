'''
para tuplas - lista imutavel ou seja o valor não muda

sintaxe nome = '', '',  -- lista sem chaves
'''

# nomes = 'maria' , 'ana'
# nomes = tuple(nomes)
# print (nomes)
# nomes = list(nomes)
# print (nomes)


lista = ['Maria' , 'Ana', 'Marta']
lista.append('João')

# lista_enumerate = enumerate(lista)

for indice, nome in enumerate(lista):
    print(indice, nome)

