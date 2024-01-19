"""
função lambda em python
a função lambda pe uma função como qualquer
outra função, porém, são funções anônimas com apenas uma linha. ou seja, tudo deve ser contido dentro de uma unica expresão

"""


lista = [

    {'nome': 'luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},

]

# forma comum que seria feita a chamada de fnção sem lambda, com lambda tudo poderia ser resumido a uma linha
# def ordena(item):
# print('PRINT', item)
# return item['nome']

# lista.sort(key=ordena)
# print(lista)

# com lambda
# lista.sort(key=lambda item: item['nome'])

# for item in lista:
# print(item)


# exemplo 3

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
