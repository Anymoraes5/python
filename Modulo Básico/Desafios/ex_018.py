"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar 
caso o usuario não digite um numero inteiro informe que não é um número inteiro
"""
try :
    n1 = input ('Digite um número inteiro: ')

    n1_int = int(n1)

    validacao = n1_int/2

    if type(validacao) is float:
        print('É impar')
    elif type(validacao) is not float:
        print('É par')

except:
    if type(n1) is not int:
        print('O número digitado não é inteiro')



