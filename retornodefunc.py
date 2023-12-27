"""
retorno de valores das funções(return)
"""

 #   def soma(x,y):
  #      return x + y

  #  soma1 = soma(2,2)
  #  soma2 = soma(3,2)

  #  print(soma1 + soma2)

   # def soma1(x,y):
    #    if x > 10:
    #        return [10, 20]
   #     return x + y

"""
args - argumentos nao nomeados
* - * args (empacotamento e desempacotamento)
"""

#lembre-se de desempacotamento


#empacotando os argumentos, quantos forem precisos, com argumentos nao nomeados
def soma(*args): #args empacota todos o resto de argumentos p n gerar erro
    total = 0
    for numero in args:
        print('total', total, numero)
        total = total + numero
        print('total', total)
    print(total)

soma(1,2,3,4,5,6)


