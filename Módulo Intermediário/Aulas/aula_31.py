import aula31_m

import importlib

print(aula31_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula31_m)
    import aula31_m

print('Fim')