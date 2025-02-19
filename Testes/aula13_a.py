''' OPERADORES LÓGICOS
and (e) or (ou) not (não)
and - todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso,
a expresão será avaliada naquele valor FALSO

São considerados Falsy (que vc já viu)
0 0.0 '' False 


tambem existe o tipo none que é 
usado para representar um não valor'''

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if condicao True:
# ...

# if entrada == 'E'and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#Avaliação de curto circuito
# print(True and False and True) # as vezes retorna o valor da condição
# print(bool(''))

if 0 and 1:
    print(True and 1)