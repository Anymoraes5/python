"""
Exercícios com funções 

Crie uma função que multiplica todos os argumentos não nomeados 
recebidos
retorne o total para uma variável e mostre o valor da variável

crie uma função fala se um número é par ou impar.
retorne se o número é par ou impar 
"""

def multiply(*args):
    print(args)
    total = 1 
    for numeros in args:
        total = total * numeros
    return total

multiplicacao = multiply(1, 2, 3, 4, 5)
print(1*2*3*4*5)
print(multiplicacao)

def validacao(numero):
    parImpar = numero % 2 == 0
    
    if parImpar:
        return(f'{numero} é par')
    return(f'{numero} é impar')

print(validacao(2))
print(validacao(3))
print(validacao(10))
print(validacao(15))

