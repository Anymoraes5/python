'''Iterando strings com while'''

#       01234567891011
nome = 'Ana Caroline'
tamanho_string = len(nome)
print (nome, len(nome))

indice = 0
while indice < tamanho_string:
    indice +=1 #reconhece o indice e soma mais um que seria a letra
    
    novo_nome = 0 #zera o contador pois agr é um novo nome
    nova_string = '' #aqui concatena a nova letra
    while novo_nome < tamanho_string: #se o novo nome for menor que o nome original 
        nova_string += nome[novo_nome] + '*' #concatenará o * a cada nova letra
        novo_nome +=1 #loop para a adição
        

print(nova_string, len(nova_string ))
