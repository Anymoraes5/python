import random

digitos9 = ''
for i in range(9):
    digitos9 += str(random.randint(0,9))   

print(digitos9)    

lista = [10 , 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista_s = []

for i in range(9):
    v = int(digitos9[i]) * lista[i]
    lista_s.append(v)
    
# print(lista_s)
soma = sum(lista_s)
# print(soma)
multiply = soma * 10   
d1 = multiply % 11
if d1 >= 10 :
    d1 = 0
    print(f'o primeiro dígito do CPF é {d1}')
else:
    print(f'o primeiro dígito do CPF é {d1}')

digito10 = digitos9 + str(d1)

lista_a = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
listad2 = []

for i in range(10):
    vl = int(digito10[i]) * lista_a[i]
    listad2.append(vl)

somad2 = sum(listad2)
# print(soma)
multipli = somad2 * 10 
d2 = multipli % 11

if d2 >= 10 :
    d2 = 0
    print(f'o segundo dígito do CPF é {d2}')
else:
    print(f'o segundo dígito do CPF é {d2}')

cpf = digitos9 + str(d1) + str(d2)    
print(cpf)

if str(d1) == cpf[-2] and str(d2) == cpf[-1]:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')



#Diferenças do código anterior para o novo

import random

digitos9 = ''
for i in range(9):
    digitos9 += str(random.randint(0,9))   #Gerador dos 9 digitos random 

digito10 = digitos9 + str(d1) # a soma do 9 números com o digito verificador 

cpf = digitos9 + str(d1) + str(d2)    #Mostra o novo cpf
print(cpf)



