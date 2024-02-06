#isinstace - para saber se objeto é de deetrminado tipo

lista = [
    'a',1,1.1,True,[0,1,2], (1,2),{0,1},{'nome' : 'Luiz'},

]

for i in lista:
    print(i, type(i)) 

for i in lista:
    if isinstance(i, set):
        print(i, isinstance(i, set)) #checar se eh instancia de set, isinstance(var, type)

