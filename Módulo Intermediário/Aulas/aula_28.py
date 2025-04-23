# print(123)
# raise ValueError('Deu erro')

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')

def int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}"  enviado.'
        )
    return True


def divide(n, d): 
    int_ou_float(n)
    
    nao_aceito_zero(d)
    return n/d

print(divide(8,'0'))