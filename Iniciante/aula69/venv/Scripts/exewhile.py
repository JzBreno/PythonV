nome = 'luiz otavio'

print(len(nome))

tamanho_nome = len(nome)
novo_nome = ''
novo_nome1 = ''
contador = 0

while contador <= tamanho_nome:
    novo_nome += nome[contador]
    novo_nome1 += novo_nome + "*"
    contador += 1
    if contador == tamanho_nome:
        break

print(novo_nome1)