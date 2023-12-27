"""
conversão de strings e variaveis
com imc
operadores and, or, not

"""
from tkinter import *
from tkinter import ttk

#colocando cores em variaveis para facilitar

co0 = '#ffffff' #branca
co1 = '#444466' #preto
co2 = '#4065a1' #azul

#criando janela grafica

janela = Tk()
janela.title('Calculado IMC')
janela.geometry('295x230')
janela.configure(bg='white')

#--------------dividindo a janela em duas partes-------------

frame_cima = Frame(janela, width=295, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0,column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1,column=0, sticky=NSEW)

#-------------- configurando frame cima --------------------------

janela_orientacao = Label(frame_cima, text='calculadora de IMC', width=23, height=1, padx=0,relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
janela_orientacao.place(x=0, y=0)

janela_linha = Label(frame_cima, text='', width=400, height=1, padx=0,relief='flat', anchor='center', font=('Ivy 1'), bg=co1, fg=co1)
janela_linha.place(x=0, y=25)

#-------------- configurando frame baixo --------------------------
#criando nome da caixa de entrada
L_peso = Label(frame_baixo, text='Insira seu Peso', height=1, padx=0,relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
L_peso.grid(row=0, column=0, sticky=NSEW, padx=3, pady= 0)
#criando caixa de entrada
e_peso = Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=10, sticky=NSEW, padx=10, pady=3)
#criando nome da caixa de entrada
L_altura = Label(frame_baixo, text='Insira sua Altura', height=1, padx=0,relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
L_altura.grid(row=1, column=0, sticky=NSEW, padx=3, pady= 0)
#criando caixa de entrada
e_altura = Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=10, sticky=NSEW, padx=10, pady=3)
#resultado
l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6,pady=12, relief='flat', anchor='center',bg=co2,fg=co0, font='Tvy 24 bold')
l_resultado.place(x=170, y=1)













janela.mainloop()


#codigo IMC
# nome1 = 'Breno'
# msg1 = f'Olá, {nome1}. bem vindo ao calculador de IMC'
# print(msg1)
# peso = float(input("digite seu peso: "))
# altura = float(input("digite sua altura: "))
# IMC = float(peso/altura*altura)

# if(IMC < 16.9 ): 
#     print("teste1")
# if(17<=IMC<=18.4): 
#     print("teste2")
# if(18.5>=IMC<= 24.9):
#     print("teste3")
# if(25>=IMC<=29.9):
#     print("teste3")
# if(30>=IMC<=34.9):
#     print("teste4")
# if(35>= IMC<= 40):
#     print("teste5")
# else:
#     print("teste6")
