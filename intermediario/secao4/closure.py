"""
closure e funções que retronam outras funções

exe:

"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return print(f'{saudacao}, {nome}')
    return saudar

#ele ira retornar a funcao interna que sera rodada quando o usuario necessitar com os dados guardados da primeira chamada
falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('boa noite')

print(falar_bom_dia)
print(falar_boa_noite)

#closure é a chamada da variavel que recbeu a função de retorno da primeira função. com o x() apos
falar_bom_dia('breno')
falar_boa_noite('mae')

#usar nomes de tupla
for nome in ['breno', 'ze']:
    falar_bom_dia(nome)