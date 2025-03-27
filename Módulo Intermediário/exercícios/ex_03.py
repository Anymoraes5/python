#Exercicio - perguntas e respostas
import string

perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2?',
        'Opções' : ['1', '2', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5 * 5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quantos é 10/2?',
        'Opções' : ['2', '4', '6' , '5', '7'],
        'Resposta' : '5',
    },
]

letras = list(string.ascii_uppercase)
questão = 0 

for i, pergunta in enumerate(perguntas, start=1):
    print(f'{i} - Pergunta: {pergunta['Pergunta']}')
    for a, op in enumerate(pergunta['Opções']):
        alt = letras[a]
        print(f' {alt}) {op}')
      
    while True:
        alternativa = input('Digite a resposta: ').strip().upper()

        if alternativa in letras[:len(pergunta['Opções'])]: 
            resposta_correta = pergunta['Opções'][letras.index(alternativa)]
            
            if resposta_correta == pergunta['Resposta']:
                print('RESPOSTA CORRETA!!!!!!')
                break 
            else:
                print('Resposta incorreta :(')
                break
        else:
            print('Digite uma letra válida!')
    



    