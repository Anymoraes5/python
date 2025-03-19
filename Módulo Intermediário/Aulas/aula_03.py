"""
Argumentos nomeados e não nomeados em funções Python 
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenas o argumento (valor)

Refatorar: editar o seu código
"""
def soma(x, y, z=None): #apos um parametro nomeado vai precisar ser nomeado
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}' , x + y)

soma(1, 2)
soma(3, 4)
soma(100, 200, 0 )

