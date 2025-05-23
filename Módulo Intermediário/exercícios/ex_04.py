"""
Crie uma função que encontra o primeiro duplicado consideirando
o segundo número como a duplicação .Retorne a duplicação consideira.

Requisitos:
    A ordem do número duplicado é considerada a partir da segunda 
    ocorrencia do número, ou seja , o número duplicado em si.
    EXEMPLO:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> retorne -1 (não tem duplicados)
        [1, 4, 9, 8, 9, 4, 8] retorna 9 
    Se não encontrar duplicados na lista, retorne -1
"""
def p_duplicado():
    ...


lista_de_lista_de_int = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_primeiro_duplicado(lista_de_lista_de_int):
    numeros_check = set()
    primeiro_duplicado = -1

    for num in lista_de_lista_de_int:
        if num in numeros_check:
            primeiro_duplicado = num
            break

        numeros_check.add(num)

    return primeiro_duplicado

for lista in lista_de_lista_de_int:
    print(lista,encontra_primeiro_duplicado(lista))