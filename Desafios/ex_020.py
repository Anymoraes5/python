'''
Faça um programa que peça o primeiro nome do usuário, se o nome tiver
4 letras ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é normal";
maior que 6 letras "seu nome é muito grande
'''
nome = input('Escreva seu nome: ')

if len(nome) == 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')
else:
    print('Nome invalido')
