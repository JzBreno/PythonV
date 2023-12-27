RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

Velocidade_Carro = 61
Local_Carro = 97

Vel_Carro_Pass_Radar_1 = Velocidade_Carro > RADAR_1 #velocidade do carro se for maior que a do radar
InfRadar = (LOCAL_1 - RADAR_RANGE) #local do radar - range
SupRadar = (LOCAL_1 + RADAR_RANGE) #local do radar + range
MenosRadar = Local_Carro >= InfRadar #local do carro esta dentro do range do radar
MaisRadar = Local_Carro <= SupRadar #local do carro esta dentro do range do radar
Carro_Passou_Radar_1 = MenosRadar and MaisRadar #local do carro esta dentro do range do radar
Carro_Multado_Radar_1 = Carro_Passou_Radar_1 and Vel_Carro_Pass_Radar_1

if Vel_Carro_Pass_Radar_1:
    print('Carro passou radar 1')
if Carro_Multado_Radar_1:
    print('carro multado radar 1')
