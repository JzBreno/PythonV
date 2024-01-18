def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador, numero):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# fazendo com lambda e testando soma original


print(
    F'FUNÇÃO LAMBDA FAZENDO A FUNÇÃO SOME EM APENAS UMA LINHA',

    executa(
        lambda x, y: x+y,
        2, 3  # argumentos que entram para suprir a condição  da lambda
    ),

    # usando a funcao soma + os 2 argumentos que precisa para função

    F'FUNÇÃO SOMA ORIGNAL FAZENDO A SOMA DELA',
    executa(soma, 2, 3)
)


# usando cria_multiplicador como função


duplicada = executa(
    lambda m: lambda n: n*m,
    2  # passamos a primeira referencia a valor

)  # duplicada vai receber a funcção de retorno da primeira função, podemos usar *args como  



print(f'usando lambda para fazer duplicada', duplicada(2))
