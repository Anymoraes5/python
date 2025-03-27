#Sets - conjuntos em python (tipo set)
'''
conjuntos são ensinados na matematica
representados graficamente pelo diagrama de venn
sets em python são mutaveis, porem aceitam apenas tipos imutaveis 

Criando um set
set(iteravel ) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados 
de iteraveis 
- eles não tem ìndexes;
- eles não garantem ordem 
- ele são iteráveis (for, in, not in)

metodos úteis:
add, update, clear, discard 
'''

# s1 = {'Ana', 2, 3} #não garante a ordem 
# print(s1)

# l1 = [1, 2, 3, 4, 3, 4, 7, 8, 3, 4]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3, 4 , [1,2,3]} não aceita lista pois é mutavel 
# print(s1)

#da pra usar o for, in , not in 
s1 = {1, 2, 3} #não garante a ordem 
print(3 in s1)
print(2 not in s1)

for n in s1:
    print(n)

