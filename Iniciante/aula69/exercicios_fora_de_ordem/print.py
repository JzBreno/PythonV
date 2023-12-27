nome = input('Digite seu nome: ')
tam_nome = len(nome)

if tam_nome > 1:
    if tam_nome <= 4:
        print('Seu nome é curto')
    elif tam_nome >= 5 and tam_nome <= 9:
        print('Seu nome tem tamaho normal')
    else:
        print('Seu nome é extremamnete grande')


