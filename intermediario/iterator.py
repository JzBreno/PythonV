#generator expression, iterables e iterators em python

iterable = ['eu', 'voce', 'nos', '__iter__']
iterator = iter(iterable)  #ou usar iter(iterable)

#generator expression, iterables e iterators em python
"""
sao funcs que sabem pausar
eles so te entrega um valor por vez
ele passa para o prox elemento quando se chama o proximo com nect()

"""
lista = [ #a lista eh salva automaticamente ocupando espaco na memmoria
    n for n in range(1000)
]

genarator = ( #salva apenas um de cada vez, indo ao proximo apenas quando next for chaamdo
    n for n in range(1000)
)


for i in genarator: #next chamado internamente
    #print(i)

#introdcao as generator functions em python
# generator = (n for n in range(1000000000))
#funcs geradoras usam yield antes de return
    
    def generator1(n=0,  maximum = 10):
        while True:
            yield n
            n += 1

            if n >= maximum:
                return


gen = generator1(n=0)
for n in gen:
    print(n)



