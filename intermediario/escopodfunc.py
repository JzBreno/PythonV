

x = 1 # escopo 1

#definindo funcao
def escopo(): # escopo 2
    global x # estou chamando o x global e agr tudo se referencia a ele
    x = 10 

    def outra_funcao(): # escopo 3
        

        x = 11
        y = 2 
        print(x, y)

    #chmando a outra funcao dentro da primeira
    outra_funcao()
    print(f'esse x esta dentro da primeira função: {x}')

print(x) # printando o x global antes de incrementar global x na funcao
escopo() # chama funcao
print(x) # continua printando o x global, a funcao nao tem retorno para alterar a variavel global
