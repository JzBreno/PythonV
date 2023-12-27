lista = ['breno', 'macho', 'teste']
i = 0
for nome in lista:
    print(f'indice: {i}, dado: {nome}')
    i += 1

#outra forma de fazer:
print('esse é o resultado da outra forma de fazer: ')
lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

#enumerate é um iterator que sera usado para mostrar o local e o conteudo, apos o primeiro uso n funciona mais
for i in enumerate(lista):
    print(i)