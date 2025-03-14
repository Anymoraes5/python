cpf = int(input('CPF: '))
print('Sem pontos e sem traços!')
cpf_str = str(cpf)


lista = [10 , 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista_s = []

for i in range(9):
    v = int(cpf_str[i]) * lista[i]
    lista_s.append(v)
    
# print(lista_s)
soma = sum(lista_s)
# print(soma)
multiply = soma * 10   
d1 = multiply % 11
if d1 >= 9 :
    d1 = 0
    print(f'o primeiro dígito do CPF é {d1}')
else:
    print(f'o primeiro dígito do CPF é {d1}')

#-----------digito 2 -------------

lista_a = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
listad2 = []

for i in range(10):
    vl = int(cpf_str[i]) * lista_a[i]
    listad2.append(vl)

# print(lista_s)
somad2 = sum(listad2)
# print(soma)
multipli = somad2 * 10 
d2 = multipli % 11
if d2 > 9 :
    d2 = 0
    print(f'o segundo dígito do CPF é {d2}')
else:
    print(f'o segundo dígito do CPF é {d2}')

if d1 == int(cpf_str[-2]) and d2 == int(cpf_str[-1]):
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')