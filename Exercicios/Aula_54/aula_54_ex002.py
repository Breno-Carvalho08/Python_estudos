"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''
import datetime #Quando quiser utilizar valores de horários (biblioteca datetime)

current_time = datetime.datetime.now() #Dentro de 'datetime' importamos a classe 'datetime' e chamamos o método 'now()'
hours = str(current_time.hour)

'''

hours = input('Informe a hora: ')


try:
    hours_check = int(hours)
    good_morning = (hours_check >= 0) and (hours_check <= 11)
    good_afternoon = (hours_check >= 12) and (hours_check <= 17)
    good_evening = (hours_check >= 18) and (hours_check <= 23)
    if good_morning:
        print('Bom dia!')
    elif good_afternoon:
        print('Boa Tarde!')
    elif good_evening:
        print('Boa noite!')
    else:
        print('Hora inválida')
except:
    print('Hora inválida')





#minutes = current_time.minute
#print(f'{minutes} minutos')
#sec = current_time.second
#print(f'{sec} segundos')



