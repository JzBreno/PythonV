
"""
try: "tenta rodar o codigo"
except: "exibe a exceção caso haja algum erro no try"

se chama de fast error
"""

numero = input("digite o numero: ")

try:
    print(f'numero digitado é {numero}')
    numero_float = float(numero)
    print(f'seu numero é {numero_float} e o dobro é {numero_float*2}')

except:
    print("Isso não é um numero")