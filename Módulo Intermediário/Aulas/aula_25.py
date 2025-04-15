'''
introdução às generator functions em python 
generator = (n for n in range (10000000))
'''

def generation (n=0):
    yield 1 #pausa execução 
    return 'ACABOU' # levanta execeção stop interation 

gen = generation(n=0)

print(next(gen))
print(next(gen))



def generation (n=0):
    yield 1 #pausa execução 
    print ('Continuando....')
    yield 2 #pausa
    print ('Mais uma...')
    yield 3 #pausa

gen = generation(n=0)

print(next(gen))
print(next(gen)) 

# yield 3 não executa pq não chamei o next 


def generation (n=0, maximum = 10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return

        

gen = generation()
for n in gen :
    print(n)

