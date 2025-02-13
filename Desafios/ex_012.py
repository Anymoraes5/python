#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Qual o valor atual do produto? \n'))
desconto = produto * 0.05
new_value = produto - desconto
print('O desconto sobre o produto foi de {:.2f} e agora está saindo por {:.2f}'.format(desconto,new_value))
