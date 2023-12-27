qt_linha = 5
qt_coluna = 5

linha = 1

while linha <= qt_linha:
    coluna  = 1
    
    while coluna <= qt_coluna:
        print(f"{linha=}\n{coluna=}")
        coluna += 1
    linha += 1

print('Acabou')