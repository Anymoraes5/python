# yield from 

def gen1():
    print('gen 1')
    yield 1
    yield 2
    yield 3
    print('fim gen 1')

def gen3():
    print('gen 3')
    yield 7
    yield 8
    yield 9
    print('fim gen 3')

def gen2(gen):
    print('gen 2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('fim gen 2')

g1 = gen2(gen1)
g2 = gen2(gen3)

for n in g1:
    print(n)
for n in g2:
    print(n)