'''
Fatiamento de string
012345678
Olá mundo
-987654321
Fatiamento[i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
'''

variavel = 'Olá mundo'
print(variavel[4:]) # do 4º digito ao fim

variavel = 'Olá mundo'
print(variavel[-8:-2]) #invertido 

variavel = 'Olá mundo'
print(variavel[0: len (variavel):1]) # 9 caracteres e 8 indices pois conta o zero
#              inicio: fim : passo  len(variavel) = ao numero de caracter

