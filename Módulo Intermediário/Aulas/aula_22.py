#dir, hasattr, getattr em python

string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
   print('Existe upper')
   print(getattr(string,metodo)()) 
else:
   print('Não existe metodo', metodo)