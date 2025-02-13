nome = input ('Qual o seu nome: ')
print ('Prazer em te conhecer {:>20}!'.format(nome)) #Vinte caracteres alianhado a direita
print ('Prazer em te conhecer {:<20}!'.format(nome)) #Vinte caracteres alianhado a Esquerda
print ('Prazer em te conhecer {:^20}!'.format(nome)) #Vinte caracteres alianhado a Centralizado 
print ('Prazer em te conhecer {:=^20}!'.format(nome)) #Vinte caracteres alianhado a Centralizado + 20 sinais

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} , \n o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end='') #{:.3f} é igual a 3 casa decimais flutuantes end = '' não quebra a linha entre os prints e se add algo nas aspas ele add mas nãop quebra a linha mesmo assim 
print('Divisão inteira é {} e potência {}'.format(di,e)) #Já o \n quebra a linha mesmo que seja em um print só

