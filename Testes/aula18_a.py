'''
introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero = input('Vou dobrar o número que vc digitar: ')

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'O dobro de {numero} é {numero_float*2:.2f}')
# else:
#     print('Isso não é um número')

try:
    print('STR:' , numero)
    numero_float = float(numero)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')
