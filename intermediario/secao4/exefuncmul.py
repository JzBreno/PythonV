#brenox vai fazer uma func que ira multiplicar todos os argumentos que entraram nele
def printa(*args):
    soma1 = 1

    for i in args:
        a = int(i)
        soma1 *= a
    return soma1    
        

lista = [2,3,4,5]
teste = 0
soma = printa(*lista)
print(f'soma antes de adicionar: {soma}')

