frase = 'O python é um linguangem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais = 0 
letra_q_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    frq_letra = frase.count(letra_atual)

    if apareceu_mais < frq_letra:
        apareceu_mais = frq_letra
        letra_q_apareceu_mais = letra_atual 

    i += 1

print('A letra que apareceu mais vezes foi: '
       f'{letra_q_apareceu_mais} que apareceu '
       f'{apareceu_mais}x')

