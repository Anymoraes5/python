'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
'''
condicao = False # mudei para quebrar o codigo
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
