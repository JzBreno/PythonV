valor = int(input())
aumento = int(input())


def adicionar(valor, aumento):
    return int(valor + (valor * aumento) / 100)


a = list(map(adicionar, valor, aumento))

