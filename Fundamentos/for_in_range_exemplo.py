inicio = input('Qual número deseja começar: ')
fim = input('Qual número deseja terminar: ')
passo = input('Ir de quantos em quantos: ')

string_sequencia = ''
try:
    inicio_check = int(inicio)
    fim_check = int(fim)
    passo_check = int(passo)

    for num in range(inicio_check, fim_check, passo_check): #range (start, stop, step) => começo, parada, passo
        string_sequencia += f'{num} ' 
   
except:
    print('Valores inválidos.')

print(string_sequencia)