import sys

import aula_30m

sys.path.append('/home')
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')