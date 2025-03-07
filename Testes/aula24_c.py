'''
Iteravel -> str, range, etc (___iter___)
iterador  -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue o seu iterador

'''
texto = iter('Ana')  #entrega o objeto iterador #.__iter__()
print(texto)

print(texto.__next__())
print(texto.__next__())
print(texto.__next__()) #quando esgota os valores apresenta erro






# numeros = range (0, 100, 8)

# for numero in numeros:
#     print(numero)

