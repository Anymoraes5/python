''' Calculadora com while '''

while True:
    n1 = input ('Digite um número: ')
    n2 = input ('Digite outro número: ')
    op = input ('o operador aritmetico (+-/*) ')

    numeros_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True #questiona se gerou erro
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são invalidos!')
        continue

    operadores_permitidos = '+-/*'

    if op not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(op) > 1:
        print('Digite apenas 1 operador!')
        continue
    print('Realizando sua conta...')
    if op == '+':
        print(n1_float + n2_float)
    elif op == '-':
        print(n1_float - n2_float)
    elif op == '/':
        print(n1_float / n2_float)
    elif op == '*':
        print(n1_float * n2_float)
    else:
        print('Não deveria chegar aqui!')

    sair = input('Quer sair? [s]im: ') .lower().startswith('s')
    print(sair)

    if sair is True:
        break