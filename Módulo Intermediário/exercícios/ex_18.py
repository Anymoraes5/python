esqueleto = input().lower()
classe = input().lower()
alimentacao = input().lower()

if esqueleto == 'vertebrado':
    if classe == 'ave' and alimentacao == 'carnivoro':
        print('aguia')
    elif classe == 'ave' and alimentacao == 'onivoro':
        print('pomba')
    elif classe == 'mamifero' and alimentacao == 'onivoro':
        print('homem')
    elif classe == 'mamifero' and alimentacao == 'herbivoro':
        print('vaca')


if esqueleto == 'invertebrado':
    if classe == 'inseto' and alimentacao == 'hematofago':
        print('pulga')
    elif classe == 'inseto' and alimentacao == 'herbivoro':
        print('lagarta')
    elif classe == 'anelideo' and alimentacao == 'hematofago':
        print('sanguessuga')
    elif classe == 'anelideo' and alimentacao == 'onivoro':
        print('minhoca')
