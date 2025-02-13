#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 
dindin = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = dindin/5.78
print('Você pode comprar U${:.2f} de dolars hoje'.format(dolar))