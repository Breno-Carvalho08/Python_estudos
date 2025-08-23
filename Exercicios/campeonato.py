import random

times_brasileiros = {
    "Sudeste": [
        "Flamengo", "Fluminense", "Vasco da Gama", "Botafogo",
        "Corinthians", "Palmeiras", "São Paulo", "Santos", 
        "Atlético Mineiro", "Cruzeiro"
    ],
    "Sul": [
        "Grêmio", "Internacional", "Juventude",
        "Athletico Paranaense", "Coritiba",
        "Avaí", "Chapecoense", "Criciúma"
    ],
    "Centro-Oeste": [
        "Goiás", "Atlético Goianiense", "Vila Nova",
        "Cuiabá"
    ],
    "Nordeste": [
        "Bahia", "Vitória", "Fortaleza", "Ceará",
        "Sport Recife", "Santa Cruz", "Sampaio Corrêa"
    ],
    "Norte": [
        "Paysandu", "Remo", "São Raimundo"
    ]
}

#Sorteio jogos
times_sudeste = set(times_brasileiros['Sudeste'])
times_sul = set(times_brasileiros["Sul"])
times_centro_oeste = set(times_brasileiros["Centro-Oeste"])
times_nordeste = set(times_brasileiros["Nordeste"])
times_norte = set(times_brasileiros["Norte"])
total_times_campeonato = times_sudeste | times_sul | times_norte | times_nordeste | times_centro_oeste
lista_times_campeonato = list(total_times_campeonato)
quant_total_times = len(lista_times_campeonato)

lista_times_sorteados = []
tabela_campeonato = []
classificados_oitavas = []
jogos = 0

print('Fase de grupos')
while quant_total_times != 0:
    time_sorteado_num = random.randint(0, quant_total_times - 1)
    time_nome_1 = lista_times_campeonato[time_sorteado_num]
    del lista_times_campeonato[time_sorteado_num]
    quant_total_times -= 1
    lista_times_sorteados.append(time_nome_1)
    gols_time_1 = random.randint(0,5)
    
    time_sorteado_num = random.randint(0, quant_total_times - 1)
    time_nome_2 = lista_times_campeonato[time_sorteado_num]
    del lista_times_campeonato[time_sorteado_num] 
    quant_total_times -= 1
    lista_times_sorteados.append(time_nome_2)
    gols_time_2 = random.randint(0,5)

    while gols_time_1 == gols_time_2:
        gols_time_1 = random.randint(0,5)
        gols_time_2 = random.randint(0,5)

    if gols_time_1 > gols_time_2:
        classificados_oitavas.append(time_nome_1)

    if gols_time_1 < gols_time_2:
        classificados_oitavas.append(time_nome_2)

    jogos += 1
    print(f'{jogos}º {time_nome_1} {gols_time_1}X{gols_time_2} {time_nome_2}')

quant_times_oitavas = len(classificados_oitavas)
classificados_quartas = []
jogos = 0

print()
print('Oitavas de Final')
while quant_times_oitavas != 0:
    time_sorteado_num = random.randint(0, quant_times_oitavas - 1)
    time_nome_1 = classificados_oitavas[time_sorteado_num]
    del classificados_oitavas[time_sorteado_num]
    gols_time_1 = random.randint(0, 5)
    quant_times_oitavas -= 1
    
    time_sorteado_num = random.randint(0, quant_times_oitavas - 1)
    time_nome_2 = classificados_oitavas[time_sorteado_num]
    del classificados_oitavas[time_sorteado_num] 
    gols_time_2 = random.randint(0, 5)
    quant_times_oitavas -= 1

    while gols_time_1 == gols_time_2:
        gols_time_1 = random.randint(0,5)
        gols_time_2 = random.randint(0,5)

    if gols_time_1 > gols_time_2:
        classificados_quartas.append(time_nome_1)

    if gols_time_1 < gols_time_2:
        classificados_quartas.append(time_nome_2)
    jogos += 1
    print(f'{jogos}º {time_nome_1} {gols_time_1}X{gols_time_2} {time_nome_2}')

quant_times_quartas = len(classificados_quartas)
classificados_semi = []
jogos = 0

print()
print('Quartas de Final')
while quant_times_quartas != 0:
    time_sorteado_num = random.randint(0, quant_times_quartas - 1)
    time_nome_1 = classificados_quartas[time_sorteado_num]
    del classificados_quartas[time_sorteado_num]
    gols_time_1 = random.randint(0, 5)
    quant_times_quartas -= 1
    
    time_sorteado_num = random.randint(0, quant_times_quartas - 1)
    time_nome_2 = classificados_quartas[time_sorteado_num]
    del classificados_quartas[time_sorteado_num] 
    gols_time_2 = random.randint(0, 5)
    quant_times_quartas -= 1

    while gols_time_1 == gols_time_2:
        gols_time_1 = random.randint(0,5)
        gols_time_2 = random.randint(0,5)

    if gols_time_1 > gols_time_2:
        classificados_semi.append(time_nome_1)

    if gols_time_1 < gols_time_2:
        classificados_semi.append(time_nome_2)

    jogos += 1
    print(f'{jogos}º {time_nome_1} {gols_time_1}X{gols_time_2} {time_nome_2}')

quant_times_semi = len(classificados_semi)
classificados_final = []
jogos = 0

print()
print('Semi-Final')
while quant_times_semi != 0:
    time_sorteado_num = random.randint(0, quant_times_semi - 1)
    time_nome_1 = classificados_semi[time_sorteado_num]
    del classificados_semi[time_sorteado_num]
    gols_time_1 = random.randint(0, 5)
    quant_times_semi -= 1
    
    time_sorteado_num = random.randint(0, quant_times_semi - 1)
    time_nome_2 = classificados_semi[time_sorteado_num]
    del classificados_semi[time_sorteado_num] 
    gols_time_2 = random.randint(0, 5)
    quant_times_semi -= 1

    while gols_time_1 == gols_time_2:
        gols_time_1 = random.randint(0,5)
        gols_time_2 = random.randint(0,5)

    if gols_time_1 > gols_time_2:
        classificados_final.append(time_nome_1)

    if gols_time_1 < gols_time_2:
        classificados_final.append(time_nome_2)

    jogos += 1
    print(f'{jogos}º {time_nome_1} {gols_time_1}X{gols_time_2} {time_nome_2}')
     
print()     
time_finalista_1 = classificados_final[0]
time_finalista_2 = classificados_final[1]
gols_time_1 = random.randint(0, 5)
gols_time_2 = random.randint(0, 5)

while gols_time_1 == gols_time_2:
    gols_time_1 = random.randint(0, 5)
    gols_time_2 = random.randint(0, 5)

print('Final')
print(f'{time_finalista_1} {gols_time_1}X{gols_time_2} {time_finalista_2}')
print()
if gols_time_1 > gols_time_2:
    print(f'CAMPEÃO: {time_finalista_1}')
if gols_time_1 < gols_time_2:
    print(f'CAMPEÃO: {time_finalista_2}')
