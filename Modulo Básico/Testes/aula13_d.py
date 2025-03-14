''' Operadores in e not in
String são iteráveis(navegar item a item)
0 1 2 3 4 5 
C A R O L I
-6-5-4-3-2-1'''

# nome = 'Otávio'
# # print(nome[2]) #utiliza chave para chmar o indice
# # print(nome[-4]) #utiliza chave para chmar o indice
# print('á' in nome) #in = estar entre  imprime = True
# print('vio' in nome) #in = estar entre
# print('z' in nome) #in = estar entre imprime = False
# print(10 * '-')
# print('vio' not in nome)
# print ('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input ('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

