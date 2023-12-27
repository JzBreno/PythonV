"Calculadora simples com WHILE"

while True:

    print("Bem vindo a calculadora Brenox")
    print("(+) para somar")
    print("(-) para somar")
    print("(*) para multiplicar")
    print("(/) para dividir")

    sinal = input("Digite o sinal ")
    match sinal:
        case "+":
            print("Você escolheu a soma")
            num1 = int(input("digite o primeiro numero aqui: "))
            num2 = int(input("digite o segundo numero aqui"))
            soma = num1 + num2
            print(f'sua soma entre {num1} e {num2} resulta em {soma}')

        case "-":
            print("Você escolheu a subtração")
            num1 = int(input("digite o primeiro numero aqui: "))
            num2 = int(input("digite o segundo numero aqui"))
            sub = num1 - num2
            print(f'sua subtração entre {num1} e {num2} resulta em {sub}')
        case "/":
            print("Você escolheu a divisão")
            num1 = int(input("digite o primeiro numero aqui: "))
            num2 = int(input("digite o segundo numero aqui"))
            div = num1 / num2
            print(f'sua divisão entre {num1} e {num2} resulta em {div}')
        case "*":
            print("Você escolheu a divisão")
            num1 = int(input("digite o primeiro numero aqui: "))
            num2 = int(input("digite o segundo numero aqui"))
            mult = num1 * num2
            print(f'sua divisão entre {num1} e {num2} resulta em {mult}')

    sair = input("Quer sair? Digite [s]im: ")
    sair = sair.lower().startswith("s")


    if sair is True:
        break