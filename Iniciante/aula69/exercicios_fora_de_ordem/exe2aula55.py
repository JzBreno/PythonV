
laço = input('"Entrar" ou ""sair"" para seguir no laço: ')

if laço == 'ficar':
    laço = True
else:
    laço = False

while laço:
    entrada = input('Digite seu horario em numero inteiro: ')
    try:
        hora = int(entrada)

        if hora >= 0 and hora <= 11:
            print(f'Bom dia, são {hora}')
        elif hora >=12 and hora <= 17:
            print(f'Boa tarde, são {hora}')
        elif hora >=18 and hora <=23:
            print(f'Boa noite, são {hora}')
        else: 
            print('Não conheço essa hora')

    except:
        print('por favor, digite apenas numeros inteiros')
    laço = input(' "ficar" ou "sair" para seguir no laço')
    if laço != True:
        break

