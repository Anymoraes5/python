"""
Faça um programa qie pergunte a hora ao usuario e, baseando-se no hórario 
descrito, exiba a saudação apropriada. ex: bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""

horario = input('Que horas são? r: ')
horario_int = float(horario)

if horario_int >= 0 and horario_int <= 11:
    print('Bom dia!')
elif horario_int >= 12 and horario_int <= 17:
    print('Boa tarde!')
else:
    print('Boa noite')
