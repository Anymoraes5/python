print('-----------Lista de compras ---------')
try:
    lista = []
    quantidade = int(input("Quantos itens deseja adicionar? "))



    for _ in range(quantidade):
        item = input("Digite um item: ")
        lista.append(item)
    for indice,item in enumerate(lista, start=1):
        print(indice, item)
    remove_item = input('Deseja excluir item da lista? [s]im  / [n]ão: ')
    if remove_item == 's':
                remove = input('Qual? R: ').strip().lower()
                if remove in lista:
                    lista.remove(remove)
                    print('\n LISTA ATUALIZADA:')
                    for indice, item in enumerate(lista, start=1):
                        print(f'{indice} - {item}')
    else:
         print(f'LISTA FINAL: {lista}')

    
    
except ValueError:
     print('Digite um número válido')
   