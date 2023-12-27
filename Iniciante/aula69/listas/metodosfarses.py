frase = 'olha so que, coisa interessante'

lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].lstrip())

print(lista_frases)