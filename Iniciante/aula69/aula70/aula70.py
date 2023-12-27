string = 'teste de string'

cont = len(string)
qtd_apareceu_mais_vzs = len(string[0])
qtd_apareceu_mais_atual = 0
letra = ''
i = 0

while i < cont:

    if  string[i] == ' ':
       i += 1
       continue

    letraatual = string[i]
    qtd_apareceu_mais_atual = string.count(letraatual)

    if qtd_apareceu_mais_vzs < qtd_apareceu_mais_atual:
        qtd_apareceu_mais_vzs = qtd_apareceu_mais_atual
        letra = string[i]
    
    print(f'letra atual é {letraatual}')
    i+=1

print(f'a letra que mais apareceu foi {letra} com {qtd_apareceu_mais_vzs} repetições')