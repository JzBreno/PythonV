"""
-sets - conjuntos em python
    sets em python sao mutaveis, porem aceitam apenas tipos imutaveis como valor interno

-criando um set
    set(iteravel) ou {1,2,3}

-sets sao eficientes para remover valores duplicado de iteraveis
    eles n tem indexes
    n garantem ordem
    sao iteraveis (for, in, not in)

-metodos uteis
    add, update, clear, discard


"""

s1 = set() # vazio
print(s1)
s1m = {'Luiz', 1,2,3} #com dados

#usando a remoçao de valores duplicados do set usando uma lista com tais valores

l1 = [1,1,2,2,3,4,4,5,5]
s1 = set(l1)
l2 = list(s1)
print(f'l2',l2)

#usando metodos uteis
print('metodos')
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Ola mundo', 1,2,3,4))
print(s1)
#s1.clear()
s1.discard('Ola mundo')
print(s1)

#operadores uteis
"""
uniao | uniao (union) - une 2 sets
interseccao & (intersection) -  itens presentes em ambos
diferenca - itens presetes apenas no set da esquerda
diferenca simetrica ^- itens que nao estao em ambos
"""

print('resultado dos operadores')
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s1 ^ s2
print(s3)