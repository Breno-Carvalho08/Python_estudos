import random

'''
CONSTANTE = "Váriaveis" que não vão mudar ao longo do programa
Muitas condições no mesmo if (ruim)
Complexidade não é bom
Simples é melhor do que complexo
Legível

'''
#Constantes
RADAR_1 = 60 #Velocidade máxima do radar
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 #Distância que o radar pega

#Variáveis
local_carro = 100
velocidade_carro = random.randrange(0, 100) #Velocidade atual do carro

#Multa radar 1
vel_carro_pass_radar_1_multa = velocidade_carro > RADAR_1
comeco_range_radar_1 = (local_carro >= (LOCAL_1 - RADAR_RANGE))
final_range_radar_1 = (local_carro <= (LOCAL_1 + RADAR_RANGE))
carro_dentro_range_radar_1 = comeco_range_radar_1 and final_range_radar_1
carro_multado_radar_1 = carro_dentro_range_radar_1 and vel_carro_pass_radar_1_multa
#Atribuir nomes as variáveis igual feito acima pode deixar seu código mais legível e diminuir a complexidade.

#Estruturas condicionais com menos complexidade de código
if carro_dentro_range_radar_1:
    print('Passou no radar 1')

if carro_multado_radar_1:
    print('Passo acima da velocidade no radar 1') 

