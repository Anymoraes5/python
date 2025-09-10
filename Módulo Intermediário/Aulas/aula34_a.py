#funções decoradoras 
# decorar = adicionar / remover / restringir 
# usar as funções decoradoras em outras funções
def fabrica_de_decor(a=None, b=None, c=None):
    def fabrica_de_funções(func):
        print('Decoradora 1')
        def aninhada(*args, **kwargs):
            print('Aninhada')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funções


@fabrica_de_decor(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decor()

soma_10_5 = soma(10, 5)
print(soma_10_5)