n = int(input())

if n == 0:
    resultado = 1
else:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

print(f"O fatorial de {n} é {resultado}")