numero = input("Digite um numero: ")
if numero.isdigit():
    numero_int = int13(numero)
    par_numero = numero_int % 2 == 0
    par_impar_texto = 'impar'
    if par_numero:
        par_impar_texto = 'par'

    print(f'O numero {numero_int} é {par_impar_texto}')
else:
    print(f'o numero {par_numero} é {par_impar_texto}')