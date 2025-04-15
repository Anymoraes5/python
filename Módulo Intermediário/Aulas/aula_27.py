#TRY, EXCEPT, ELSE e FINALLY



try:
    a = 18
    b = 0 
    print ('Linha 1 '[1000])
    c = a/b 
    print('linha 2')

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: #indica qual variavel eu quero jogar a instacia do erro 
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__) #chama no erro a classe e o nome 
except Exception:
    print('Erro desconhecido ')

print('Continuar')