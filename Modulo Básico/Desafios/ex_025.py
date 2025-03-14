#----------------DESAFIOS DO BEECROWD-------
# r = input()

# r_float = float(r)

# print(f'A={(r_float**2)*3.14159:.4f}')

#-------------------------------------------

# nome = input()
# salario = float(input())
# vendas = float(input())

# print(f'TOTAL = R$ {(vendas*0.15)+salario:.2f}')

#-------------------------------------------------

# r = float(input())

# print(f'VOLUME = {(4.0/3) * 3.14159 * (r**3):.3f}')

#---------------------------------------------------
valor = float(input())

print('NOTAS:')
nota100 = valor // 100
resto100 = valor % 100
nota50 = resto100 // 50
novo_valor = valor - (nota100*100) - (nota50*50)
nota20 = novo_valor // 20
nota10 = nota20 // 10
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20)
nota5 = novo_valor // 5
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) - (nota5*5)
nota2 = novo_valor // 2


print(f'{nota100:.0f} nota(s) de R$ 100.00')
print (f'{nota50:.0f} nota(s) de R$ 50.00')
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print (f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')

print ('MOEDAS:')
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) - (nota5*5) - (nota2*2)
moeda1 = novo_valor // 1
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) - (nota5*5) - (nota2*2) - (moeda1*1)
moeda050 = novo_valor // 0.50
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) \
                        - (nota5*5) - (nota2*2) - (moeda1*1) - (moeda050*0.50)
moeda025 = novo_valor // 0.25
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) \
                        - (nota5*5) - (nota2*2) - (moeda1*1) - (moeda050*0.50) \
                           - (moeda025*0.25)
moeda010 = novo_valor // 0.10
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) \
                        - (nota5*5) - (nota2*2) - (moeda1*1) - (moeda050*0.50) \
                           - (moeda025*0.25) - (moeda010*0.10)
moeda005 = novo_valor // 0.05
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) \
                        - (nota5*5) - (nota2*2) - (moeda1*1) - (moeda050*0.50) \
                           - (moeda025*0.25) - (moeda010*0.10) - (moeda005*0.05)
moeda001 = int(novo_valor / 0.01)
novo_valor = valor - (nota100*100) - (nota50*50) - (nota20*20) \
                        - (nota5*5) - (nota2*2) - (moeda1*1) - (moeda050*0.50) \
                          -  (moeda025*0.25) - (moeda010*0.10) - (moeda005*0.05) - (moeda001*0.01)


print(f'{moeda1:.0f} moeda(s) de R$ 1.00')
print (f'{moeda050:.0f} moeda(s) de R$ 0.50')
print(f'{moeda025:.0f} moeda(s) de R$ 0.25')
print(f'{moeda010:.0f} moedas(s) de R$ 0.10')
print (f'{moeda005:.0f} moeda(s) de R$ 0.05')
print(f'{moeda001:.0f} moeda(s) de R$ 0.01')