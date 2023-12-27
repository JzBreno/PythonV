"""
são tipos imutaveis, que não se pode mudar o valor na variavel apos preencher
str, int,float, bool
são objetos que podem usar metodos para fazer coisas 

"""
string = 'Luiz Otavio'
outra_variavel = f'{string[:3]}{string[4:]}'

print(f'a nova frase é essa, {outra_variavel}, após retirar o ""Z""')
print(f'a frase antiga é essa, {string}')