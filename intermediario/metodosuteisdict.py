pessoa = {
    'nome' : 'luiz otavio',
    'sobrenome' : 'miranda',
    #'idade' : 18,
    'altura': 1.8,
    'endereco' : [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ],
}

#metodos
#len retorna quantas chaves tem nesse dicionario

#len(pessoa)
#print(len(pessoa))

#print(list(pessoa.keys())) #dict.keys() retorna as chaves, usat list ou tuple faz a coersao para oos tipos e ver
#print(list(pessoa.values())) # retorna os valores do dict
#print(list(pessoa.items())) #retorna os items do dict

#chamar iterador para mostrar as chaves, valores e items

#for chave in pessoa: 
    #print(chave)

#for valores in pessoa.values():
    #print(valores)

#for items, valores in pessoa.items():
    #print(items)
    #print(valores)

#setdefault serve para evitar excessoes em valores que sao pedidos e nao existem nodict, n afeta o preenchimento caso necessite

pessoa.setdefault('idade', 0)
print(pessoa['idade'])