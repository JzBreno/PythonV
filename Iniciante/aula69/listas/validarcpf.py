cpf = '33427873099'
nove_digitos = cpf[:9] 
contador_regressivo_1 = 10
resultado_digito1 = 0
digito2 = 0
#fazer o digito 1
for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito1 = (resultado_digito1*10) % 11
digito1 = digito1 if digito1 <=9 else 0
print(f'digito 1: {digito1}')

#fazer digito 2
resultado_digito2 = 0

if digito1 != None: #checar se digito 1 esta preenchido
    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo_2 = 11

    for digito in dez_digitos: 
        resultado_digito2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -=1
    
    digito_2 = (resultado_digito2*10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    print(f'digito 2: {digito_2}')
else:
    print('o digito 1 não foi preenchido!')

