"""
Introdução às funções (def) em python 
Funções são trechos de código usados para 
replicar determida ação ao longo do seu código.
Ele podem receber valores para parâmetros(argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam none(nada)
"""
# def Print(a, b, c):
#     print(a, b, c)

# Print(1, 2, 3)

def saudacao(nome='Sem Nome'):
    print(f'Olá {nome}!')

saudacao('Ana')
saudacao('ALAL')
saudacao()