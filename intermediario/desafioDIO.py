def mostrar(lista):
    print('Lista de itens:')
    for i in lista:
        print(f'-',i)



lista = []


for i in range(3):
    lista.append(input())

mostrar(lista)


