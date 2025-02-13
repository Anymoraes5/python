#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area/2
print('A sua parede tem {} de área e será necessário {} litros de tinta para pintá-la'.format(area,tinta))