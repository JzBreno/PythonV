string = 'nome do brenox'

i = 0

while i < len(string):
    letra = string[i]
    if letra is ' ':
        print(f'achei o espaço, esta no espaço {i+1}')
        break 
    print(letra)
    i += 1
else:
    print('o else foi exec')

print('fora do while')