'''
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Podem receber vários parâmetros (argumentos) e retornar valores específicos.
Por padrão, funções Python retornam None (nada).
'''

def funcao_test(a): #Parâmetro é o nome da "variável" dentro dos parênteses
    print('Ola')

funcao_test('') #Argumento é o valor passado para o parâmetro no momento da execução da função.

def funcao_test2(nome='Sem nome'): #Caso não seja passado argumentos para a função quando ela for chamada, irá utilziar o 'Sem nome'
    print('Ola, {}!'.format(nome))

funcao_test2('Breno')
funcao_test2()



#Argumentos e Parâmetros nomeados
def soma(x, y, z = None): #Também é possível atribuir valores nos parâmetros (eles ficam como padrão na chamada da função)
    if z is None:
        print(f'{x=} {y=} | x + y = {x + y}')
    else:
        print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')

soma(1,2)
#Uma boa prática é chamar tudo nomeado ou nenhum nomeado
soma(y = 2, x = 3, z=0) #Argumento nomeado com sinal de igual