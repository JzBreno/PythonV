"""
map serve para usar varias coisas de uma so vez diretamente
map(funcao, dadosdenetrada)

"""
kmh = [20,10,30]

mph =  list(map(lambda x : x/1.61, kmh))

#list comprehension
breno = [x/1.61 for x in kmh]
print(breno)