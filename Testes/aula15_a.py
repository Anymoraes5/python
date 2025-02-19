'''
Formatação basica de strings
s - string
d - int 
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro 
Sinal - + ou - 
ex.: 0>-100, .1f
= - força o número a aparecer antes dos zeros
conversion flags - !r !s !a
'''

variavel = 'ABC'
print (f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.23983929:0=+10,.1f}.')
