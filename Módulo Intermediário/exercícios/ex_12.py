a, b = map(int, input().split())

cardapio = {
    1 :  4.00,
    2 : 4.50,
    3 : 5.00,
    4 : 2.00,
    5 : 1.50,
}

total = 0 

if a in cardapio:
    total += cardapio[a]*b
    print(f'Total: R$ {total:.2f}')
