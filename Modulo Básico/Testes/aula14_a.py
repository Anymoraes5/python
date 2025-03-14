''' Interpolação básica de strings (parecido com o format)
s - string
d e i - int
f - float
x e x - Hexadecimal (abcdef123456789)'''

nome = 'Luiz'
preco = 1000.95897643
# variavel = 'Luiz, o preço total foi R$1000.95897643'
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15))