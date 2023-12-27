#exercio de criar uma lista
lista = ['lista de compras']
leitor_opcao = ''
while(True):
    print('Você deseja (1) - inserir, (2) - apagar, (3) - listar')
    leitor_opcao = int(input('digite a opção de deseja: '))

    match leitor_opcao:
        
        case 1:
            lista.append(input('digite o que deseja inserir: '))
            
        case 2:
            lista.pop(int(input('Digite qual item deseja apagar: ')))
        case 3:
            for i in enumerate(lista):
                print(i)
        case _:
            print('valor invalido')
            continue