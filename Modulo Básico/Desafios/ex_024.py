'''
Faça um jogo para o usuário adivinha qual a palavra secreta.
- você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para o usuário digitar
apenas uma letra
- qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta
    - se a ketra digitada estiver na palavra secreta; exiba a letra;
    -se a letra digitada não estiver na palavra secreta; exiba *.
    faça a contagem de tentativas do seu usuario
'''
print('--------------JOGO DA FORCA---------------')
palavra_secreta = 'paralelepipedo'
letras_acertadas = ''
tentativa = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativa += 1

    if len (letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 

    palavra_formada = ''
    for letra_oculta in palavra_secreta: 
        if letra_oculta in letras_acertadas:
            palavra_formada += letra_oculta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!!!')
        print(f'número de tentativas {tentativa}' , tentativa < 10)

    elif tentativa > 10 and palavra_formada != palavra_secreta:
        print (f'VOCÊ PERDEU A PALAVRA ERA {palavra_secreta.upper()}')


