lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)

'''
Cuidados com dados mutaveis
= - copinado valor (imutavel)
= - aponta para o mesmo valor na memoria (mutavel)
'''

# nome = 'ANA'
# outra = nome
# nome = 'MARTA'
# print(nome)
# print(outra)

lista_a = ['luiz' , 'Maria']
lista_b = lista_a

lista_a[0] = 'ajajaj'
print(lista_b)
