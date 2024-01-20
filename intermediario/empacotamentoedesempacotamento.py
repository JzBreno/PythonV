# empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a

# print(a, b)

# pessoa = {
#    'nome': 'Aline',
#    'sobrenome': 'Souza',

# }

# for i in pessoa.values():
#    print(i)  # entrga os valores a i

# metodos usaveis
"""
metodos usaveis em dicionarios
.values() - entrega os valores 
.items() - entrega uma tupla com ('chave', 'Valor') em STRING

"""

# passando as chaves e valores em tupla para cada variavel, desempacotamento
# a, b = pessoa.items()
# print(f'usando .items() para mandar tupla com (cahve, valor)', a, b)

# (a, a2), (b, b2) = pessoa.items()
# print(f'usando desempacotamento interno para cada variavel receber, chave e valor', a, a2)
# print(f'usando desempacotamento interno para cada variavel receber, chave e valor', b, b2)


# for chave, valor in pessoa.items():
#    print(f'usano o iterator para add cada chave e valor as duas variaveis diretamente', chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',

}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,

}

# extraindo dicionarios para um terceiro com ** 2 asteriscos
pessoa_completa = {**pessoa, **dados_pessoa}


# args e kwargs
# args (ja vimos)
# kwargs - keywored arguments (argumentos nomeados)


def mostrar_argumentos(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


mostrar_argumentos(**pessoa_completa)
