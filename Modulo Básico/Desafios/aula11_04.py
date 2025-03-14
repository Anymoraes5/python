'''print ("jogo de adivinhação") atividade 1

jo1 = int(input("Escolha um número de 1 a 10: "))

jo2 = int(input ("para tentar adivinhar escolha um numero de 1 a 10: "))


if jo1 < 10 and jo2 < 10 :
    print('       Valor valido      ')
elif jo1 > 10 and jo2 < 10:
    print ('erro!!! valor 1 inválido')
else :
    print ('erro !!! valor 2 inválido')
while jo1 != jo2 and (jo1 < 10 and jo2 <10) : 
    match input("errou, quer tentar novamente? \n ( escolha s/n): "):
        case "s":
            jo2 = int(input ("para tentar adivinhar escolha um numero de 1 a 10: "))
        case "n":
            print ('finalizado')

else :
    print ('acertou')'''

    
     

'''while jo1 != jo2 : 
    match input("errou, quer tentar novamente? \n ( escolha s/n): "):
        case "s":
            jo2 = int(input ("para tentar adivinhar escolha um numero de 1 a 10: "))
        case "n":
            print ('finalizado')
else:
    print('acertou') '''       

'''while (jo1 != jo2) :
    print('voce errou!')
    jo2 = int (input ("para tentar adivinhar novamente escolha um numero de 1 a 10: "))

else:
    print ('acertou')'''
    


'''if jo2 > 10 and jo1 > 10:
    print('erro!')

elif jo1 == 1 and jo2 ==1:
    print('você acertou')
elif jo1 == 2 and jo2 == 2:
    print('voce acertou')
elif jo1 == 3 and jo2 == 3 :
    print == ('voce acertou')
elif jo2 == 4 and jo1==4:
    print('voce acertou')
elif jo2 == 5 and jo1==5:
    print('voce acertou')
elif jo2 == 6 and jo1 == 6:
    print('voce acertou')
elif jo2 == 7 and jo1 == 7:
    print('voce acertou')
elif jo2 == 8 and jo1 == 8:
    print('voce acertou')
elif jo2 == 9 and jo1 == 9:
    print('voce acertou')
elif jo2 == 10 and jo1 == 10:
    print('voce acertou') '''


''' atividade 2 '''
print ('AGENDA')
nome = str (input ('digite o nome: '))
telefone = int (input('digite o numero ( + ddd): '))


while :
    match input('deseja adicionar mais pessoas? \n (s = sim n= nao) '):
        case  "s" :
            nome = str ('digite o nome: ')
            telefone = int ('digite o numero ( + ddd): ')
else:
    print('finalizado')



