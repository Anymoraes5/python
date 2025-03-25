"""
Exercicios 
Crie Funções que duplicam, triplicam e quadriplicam 
o número recebido como parâmetro
"""

#--------------jeito 1----------------

# x = 2

# def dobro(dobro):
#     return x * 2

# def triplo(triplo): 
#      return x * 3

# def quadruplo(quadruplo):
#     return x * 4

# d = dobro(x)
# t = triplo(x)
# q = quadruplo(x)

# print(d,t,q)

#-----------jeito 2-------------------

def equacao(numero):
    def calcular():
        return f'{numero * 2} {numero * 3} {numero * 4}'
    return calcular
    

calculo = equacao(1)
print(calculo())

#---------------jeito 3------------------

def criar_mult(mult):
    def multplicar(num):
        return num * mult
    return multplicar

d = criar_mult(2)
t = criar_mult(3)
q = criar_mult(4)

print(d(2))
print(t(2))
print(q(2))