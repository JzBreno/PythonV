import os
palavra_secreta = 'primeiro'
contagem = 0
letra_digitada = ''
letra_acertadas = ''

i = 0
while True:
    i = 0
    letra_digitada = input('digite uma letra: ')

    if len(letra_digitada) > 1: #tamanho > 1 na letra, ele volta ao inicio
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta: #se a letra estiver na palavra, ele entra
       letra_acertadas += letra_digitada
       print('sua letra tem na palavra')


        

    for letra_secreta in palavra_secreta:
            if letra_secreta in letra_acertadas:
              print(letra_secreta)
              i += 1
            else:
                print('*')
                
    
    if i == len(palavra_secreta):
        print('parabens, você acertou a palavra!')
        print(palavra_secreta)
        print(f'você teve {i} repetições para acertas')
        break