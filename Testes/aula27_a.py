
'''
split e join com list e str 
split - divide uma string
join - une uma string 
'''

frase = 'De qualquer jeito seu sorriso, vai ser meu raio de sol'
lista_palavras = frase.split(' ')


for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

print(lista_palavras)