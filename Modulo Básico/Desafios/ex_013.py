#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Digite seu salário: '))
aumento = salario * 0.15
n_salario = salario + aumento
print('Seu salário teve ajuste de {:.2f} e agora está {}'.format(aumento,n_salario))