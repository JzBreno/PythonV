perguntas = [
    {
        'perguntas' : 'Quanto é 2+2? ',
        'opcoes' : ['1', '2', '3', '4', '5'],
        'resposta' : '4',
    },
    {
        'perguntas' : 'Quanto é 5*5? ',
        'opcoes' : ['25', '2', '20', '10', '5'],
        'resposta' : '25',
    },
    {
        'perguntas' : 'Quanto é 10/2?',
        'opcoes' : ['4', '5', '3', '0', '1'],
        'resposta' : '5',
    }

]

def checkpergunta(resp,*args):
    if args[0]['resposta'] == resp: 
        print('Resposta Certa!')
        return True
    print('Resposta Errada!')
    return False

for i in perguntas:
    bandeira = False
    while bandeira == False:    
        print(*i['perguntas'])
        print('Opções: ',*i['opcoes'])

        resp = input('Digite sua resposta: ')

        bandeira = checkpergunta(resp, i )

