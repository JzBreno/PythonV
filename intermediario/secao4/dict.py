#inicio do estudo de dicionarios, dicts

#pessoa = {
    #'nome' : 'luiz otavio',
   # 'sobrenome' : 'miranda',
   # 'idade' : 18,
   # 'altura': 1.8,
   # 'endereco' : [
   #     {'rua': 'tal tal', 'numero': 123},
   #     {'rua': 'outra rua', 'numero': 321}
   # ],
#}

#pessoateste = {}
#pessoateste['nome'] = 'Breno sousa'
#print(pessoateste['nome'])

#iniciando um dict do zero, exemplificar o CRUD

teste = {}

chave = 'nome'
chave2 = 'sobrenome'
chave3 = 'nome completo'
teste[chave] = input('nome: ')
teste[chave2] = input('sobrenome: ')
teste[chave3] = teste[chave] +' '+ teste['sobrenome']

print(teste)

print(f'nome: {teste[chave]}')
print(f'sobrenome: {teste[chave2]}')
print(f'nome completo: {teste[chave3]}')

lista = []
lista.append(teste)

print(lista)
print(lista[0])

