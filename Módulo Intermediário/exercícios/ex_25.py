# Exercicio - unir listas 
# crie uma função zipper 
# o trabalho dessas funcoes será unir duas listas
# use todos os valores da menor lista 
# ex: ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA','SP', 'MG', 'RJ']



def zipper(l1, l2):
    intervalo_max = min(len(l1), len(l2))
    return [
        (l1[i], l2[i])i for i in range(intervalo_max)
    ]

cid = ['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla = ['BA','SP', 'MG', 'RJ']
zipper(cid,sigla)