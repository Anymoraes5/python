a, b, c = map(float, input().split())

delta = (b**2) - 4*a*c

if a == 0:
    print('Impossivel calcular')
elif delta < 0:
    print('Impossivel calcular')
else:
    b_neg = b*(-1)

    baskara1 = (b_neg + delta **0.5)/ (2*a)
    baskara2 = (b_neg - delta**0.5)/ (2*a)

    print(f'R1 = {baskara1:.5f}')
    print(f'R2 = {baskara2:.5f}')