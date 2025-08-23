'''
Introdução Try/Except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar o código
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_sem_espacos = nome.replace(' ', '')

try:
    nome_str = nome_sem_espacos.isalpha()
    if nome_str:
        #Caso o valor não seja um número, o programa já para nessa linha e vai ditero para o except.
        idade_int = int(idade) #Erro identificado, vai para o except.
        print(f'Seu nome é {nome} e sua idade é {idade_int} anos')
    else:
        print('Nome inválido')
except:
    print('Os dados do nome ou da idade estão incorretos')


#Aprofundando - Forma correta de tratar as exceções em python

try:
    a = 10
    b = 0
    print('Linha 1'[1000])
    c = a / b

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('Msg:', error)
    print('Nome:', error.__class__.__name__)
except Exception: #Exception é a maior classe dos erros, tratando qualquer erro
    print('ERRO DESCONHECIDO')

