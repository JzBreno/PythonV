"""
listas em python
tipo list - Mutavel
suporta varios reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +...
"""
import os
string = 'ABCDE' #5 caracteres (len)
#         01234
lista = [123, True, 'Luiz Otavio', 'Masculino']
#print(bool([])) #falsy
#print(lista, type(lista))

for i in lista:
    print(i)
    print(type(i))

print(' ')
lista[2] = 'Breno'

for i in lista:
    print(i)
    print(type(i))
