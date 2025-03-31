n = int(input())

nota_100 = n // 100; #quantas de 100
nota_50 = (n % 100) // 50
nota_20 = (n % 50 ) // 20
nota_10 = (n - (nota_100 * 100) - (nota_50 *50) - (nota_20*20)) // 10
nota_5 = (n - (nota_100 * 100) - (nota_50 *50) - (nota_20*20) - (nota_10*10)) // 5
nota_2 = (n - (nota_100 * 100) - (nota_50 *50) - (nota_20*20) - (nota_10*10) - (nota_5*5)) // 2
nota_1 = (n - (nota_100 * 100) - (nota_50 *50) - (nota_20*20) - (nota_10*10) - (nota_5*5) - (nota_2*2)) // 1

print(n)
print(f'{nota_100} nota(s) de R$ 100,00')
print(nota_50, 'nota(s) de R$ 50,00')
print(nota_20, 'nota(s) de R$ 20,00')
print(nota_10, 'nota(s) de R$ 10,00')
print(nota_5,'nota(s) de R$ 5,00')
print(nota_2, 'nota(s) de R$ 2,00')
print(nota_1, 'nota(s) de R$ 1,00')
