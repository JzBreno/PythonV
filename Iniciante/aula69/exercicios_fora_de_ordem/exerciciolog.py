
numero = int(input("Digite um numero inteiro"))

try:
    print(f'o numero {numero} e ele é float? `{numero is int}')
    if numero % 0 != 1:
        print(f'o numero {numero}é par')
    else:
        print(f'o numero é impar')
        
except:
    print(f'o numero não é inteiro!')

