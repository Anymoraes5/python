a, b, c = map(float, input().split())

lista = [a, b, c]

a, b, c = sorted([a, b, c], reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')


elif (a**2) == ((b**2)+(c**2)):
    print('TRIANGULO RETANGULO')
    if a == b or a==c or b==c:
        print('TRIANGULO ISOSCELES')
    elif a == b == c:
        print('TRIANGULO EQUILATERO')


elif (a**2) > ((b**2) + (c**2)):
    print('TRIANGULO OBTUSANGULO')
    if a == b or a==c or b==c:
        print('TRIANGULO ISOSCELES')
    elif a == b == c:
        print('TRIANGULO EQUILATERO')

elif (a**2) < ((b**2) + (c**2)):
    print('TRIANGULO ACUTANGULO')
    if  a == b or a==c or b==c:
        print('TRIANGULO ISOSCELES')

    elif a == b == c:
        print('TRIANGULO EQUILATERO')


elif a == b or a==c or b==c:
    print('TRIANGULO ISOSCELES')


elif a == b == c:
    print('TRIANGULO EQUILATERO')


