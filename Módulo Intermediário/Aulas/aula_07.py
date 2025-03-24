def soma(*args):
    print(args)
    total = 0 
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5
outrasoma = soma(*numeros)
print(outrasoma)
