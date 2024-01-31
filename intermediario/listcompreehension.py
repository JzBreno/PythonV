"""
list comprehension em python
list comprehnsion é uma forma rapida para criar listas
a partir de iteraveis.

"""

# numeros na lista com for

lista = []

for numero in range(10):
    lista.append(numero)

# fazendo com list comprehension
# logias podem ser colocadas a esquerda do for
lista = [numero for numero in range(10)]
print(f'esse', lista)


# mapeamento de dados com list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },

]

# mapeamento
novo_produto = [{**produto, 'preco': produto['preco'] * 1.05}
                if produto['preco'] > 20 else {**produto}
                for produto in produtos]

print(*novo_produto, sep='\n')
