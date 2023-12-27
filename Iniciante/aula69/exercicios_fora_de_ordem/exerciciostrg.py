nome = input(('Digite seu Nome: '))
idade = int(input(('Digite sua Idade: ')))
if nome and idade != 0:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a oprimeira letra do seu nome é {nome[0:1]}')
    print(f'a ultima letra do seu nome é {nome[24:25]}')
else:
    print("Você não digitou nada!")
