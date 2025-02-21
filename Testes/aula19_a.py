'''
constante = "variaveis" que não vão mudar
muitas condições no mesmo if (ruim)
    <- contagem de complexidade(ruim)
'''

velocidade = 65 #velocidade atual do carro
local_carro = 101 #local que o carro está na estrada

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_car_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)  

if vel_car_pass_radar_1:
    print('Passou da velocidade no radar 1')

if vel_car_pass_radar_1 and carro_multado_radar_1:
    print('carro multado em radar 1')

else: 
    print('Não foi multado')
