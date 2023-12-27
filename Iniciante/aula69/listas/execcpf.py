#exercicio com o CPF

cpf = [6,1,6,7,7,6,9,9,3,1,0]
i = 0
soma9valores = 0
multi = 0
somaresultado = 0

#somando os digitos em uma variavel que ira guardar a soma dos 9 primeiros valores
while i <= 8:
    soma9valores += cpf[i]
    i += 1

i = 0
j = 10

#multiplica os digitos por uma regressiva apartir de 10
while i <=8 and j > -1:
    multi = cpf[i]
    

    print(f'o valor é {cpf[i]} X {j}')
    multi = cpf[i] * j
    j -= 1
    print(f' = {multi}')

    i += 1

    somaresultado += multi

if somaresultado % 11 > 9:
    

print(somaresultado)
