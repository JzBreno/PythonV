"append, insert, pop, del, clear, extend, +"
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista3 = lista1 + lista2 #soma as duas listas em uma lista maior 
print(lista3)

lista1.extend(lista2) #essa ação extende na "lista1" a concatenação, ele mexe diretamente no primeiro endereço do extend
print(lista1) 