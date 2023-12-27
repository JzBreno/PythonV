"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis:

    append, insert, pop, del, clear, extend, +
create read Update, Delete
Criar, ler, aleterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2, 3, 4]

for lista1 in lista:
    print(lista1)

numero = lista[2]
print(numero)

lista[2] = 300
numero = lista[2]
print(numero)

del lista[2] # dele valor da lista e o posterior tomara o indice
print(lista[2])

lista.append(50) # ira adicionar valor no fim da lista
print(lista)

lista.pop()# pop remove o ultimo valor da lista, dentro das () pode passar o indice que desja remover, default sera o ultimo
ultimo_valor = lista.pop() #o ultimo valor que vai ser removido sera adicionado a variavel
print(f'a lista sem o ultimo valor: {lista}')
print(f'o ultimo valor era {ultimo_valor}')