a, b = 1, 2
a, b = b, a

# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# print()
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)


pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}


dados_pessoa = {
    'idade' : 16,
    'altura' : 1.58,
}

pessoa_completa = {**pessoa, 'chave' : 1, **dados_pessoa} #desempacotamento


# print(pessoa_completa)

#args e kwargs
# arg (nomeados)
#kwargs - keyword arguments (argumento nomeados)

def mostro_argumentos_nomeado(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#mostro_argumentos_nomeado(nome='Joana', qlq=123)
#mostro_argumentos_nomeado(**pessoa_completa)

configuracoes = {
    'args1' : 1,
    'args2' : 2,
    'args3' : 3,
    'args4' : 4,
}

mostro_argumentos_nomeado(**configuracoes)