"""
cuidados com dados mutaveis
= - copiado o valor(imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
o metodo copy, ira copiar e nao fazer referencia
"""

lista1 = ['luiz', 'maria'] #essa estrutura mutavel ocupa um espaço dememoria com essas informações
lista4 = lista1.copy()
lista2 = lista1 # a lista2 ira apontas para o espaço de memoria dalista1, na lista 1 estara armaxenado os valores, n existe copia e sim um ponteiro
lista1.append('Brneox') #muatara a lista1 e ira refletir na lista2, pois a lista2 é um ponteiro

print(f'lista 2: {lista2}')
print(f'lista 4: {lista4}')