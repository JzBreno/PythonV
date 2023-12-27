
nome = input("Digite seu Nome: ")
num = len(nome)
finalnome = " "
novonome = " "
flag = 0

while flag < num:

    if nome[flag] == nome[0]:

        novonome = "*" + nome[flag] + "*"    
    else:
        novonome = nome[flag]
        novonome = novonome + "*"
    
    finalnome += novonome
    flag += 1

print(finalnome)