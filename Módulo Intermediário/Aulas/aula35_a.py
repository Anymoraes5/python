def param_decor(nome):
    def decorador(func):
        print('Decorador', nome)

        def New_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return New_function
    return decorador

@param_decor(nome='primeiro')
def soma(x, y):
    return x + y

dez_5 = soma(10, 5)
print(dez_5)