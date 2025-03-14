'''
Listas em python 
tipo list - Mútavel
Suporta vários valores de qualquer tipo
conhecimento reutilizaveis  - indices e fatiamento 
metodos úteis: append, insert, pop, del, clear, extend
'''

#           01234
#           -54321
string =    'ABCDE' # 5 caracter

# print (bool(lista)) #lista
# print(lista, type(lista))


#        0     1     2     3    4
lista = [123, True, 'Ana', 1.9, []]
lista.append('mm')
remove_valor = lista.pop()
lista.append(50)
lista.append(60)
lista.append('haha')
lista.append (1233)
del lista[-1]
lista.clear()

print (lista)