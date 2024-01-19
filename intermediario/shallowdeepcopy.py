"""
metodos uteis para dicts 
len - quantas chaves ~
keys - iteravel com as chaves
values - iteravel com valores
items - ietravel com chaves e valores
setdefault - add valor se a chave n existe(evitar execessao)
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga ultimo item adicionado
update - atualiza um dicionario com outro
"""

pessoa = {
    'nome' : 'Luiz Miranda',
    'sobrenome': 'Miranda',
    'idade': 900,
}

d1 = {
    'c1': 1,
    'c2': 2,
    'l1' : [0,1,2]
}
#copia 
d2 = d1 # cria copia que aponta para dict e nao cria outro dic, afeta diretamente ao primeiro dicionario
print(f'd1 antes de mudar em d2: {d1}')
d2['c1'] = 1000
print(f'd1 depois: {d2}')

d2 = d1.copy() #copia rasa, copia dados imutaveis e aponta para estruturas mutaveis no primeiro 

