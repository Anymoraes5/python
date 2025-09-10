#funções decoradoras 
# decorar = adicionar / remover / restringir 
# usar as funções decoradoras em outras funções

def criar_func(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(resultado)
        print('foi decorado')
        return resultado
    return interna

@criar_func #acucar sintatico para usar funçao sem necessaria chamando no final 
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

inverte_string_check_parametro = criar_func(inverte_string)
invertida = inverte_string('123')
print(invertida)