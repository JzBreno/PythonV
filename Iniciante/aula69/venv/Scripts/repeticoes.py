"""
while repete o bloco enquanto a condiçãos for verdadeira
use uma flag, use para parar o while
""" 
flag = True

while flag:

    print('Loucura!')
    continuar = input("Continuar? ""SIM"" ou ""NAO""  ")
    continuar1 = continuar.upper

    if continuar1 == 'SIM':
        print('OK, vamos continuar')
    else:
        print('Até mais, se vemos por ai')
        break

contador = 0
while contador < 10:
    print('EITA')
    contador += 1 #soma valor do contador + 1

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

# o continue volta o codigo pro começo do laço, não segue o resto do codigo
contador = 0 
while contador < 100:

    contador += 1 

    if contador == 6: #pulara o numero 6
        continue

    print(contador)

    if contador == 40:
        break

    