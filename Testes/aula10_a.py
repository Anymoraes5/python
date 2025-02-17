nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = int(input('Digite 1º número: '))
numero_2 = int(input('Digite 2º número: ')) # -------------MANEIRA INCORRETA

print(f'A soma dos números é: {numero_1 + numero_2}')


num1 = input('dgt 1º número: ')
num2 = input('dgt 2° número: ')

int_num1 = int(num1)
int_num2 = int(num2)  #conversão que previne quebrar o codigo na primeira linha 

print(f'A soma é {int_num1+int_num2}')