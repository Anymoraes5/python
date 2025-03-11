'''
Faça uma lsta de compras com listas
o usuário deve ter a posibilidade de inserir apagar e listar valores da sua lista
não permita que o programa quebre com erros de indice inexistentes.
'''


print('------LISTA DE COMPRAS------')
try:
    lista = []

    while True:
        item = input ('Deseja inserir item? [s]im [n]ão: ').lower()
        if item == 's':
            n_item = input('Qual? r: ').lower()
            lista.append(n_item)
            for indice, item in enumerate (lista, start=1):
                print(f'{indice} - {item}')
        elif item == 'n' :
            remove = input('Deseja apagar algum item? [s]im [n]ão: ').lower()
            if remove == 's':
                remove_item = input('Qual? R: ').lower()
                if remove_item in lista:
                    lista.remove(remove_item)
                    for indice, item in enumerate(lista, start=1):
                        print(f'{indice} - {item}')
            else:
                print('fim da remoção')
                continue

        else:
            print('Fim da lista')
            break
except:
    ...