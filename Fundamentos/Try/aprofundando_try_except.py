#Forma correta de tratar as exceções em python

try:
    a = 10
    b = 0
    print('Linha 1'[1000])
    c = a / b

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: #Pegando o erro em uma variável
    print('Msg:', error)
    print('Nome:', error.__class__.__name__)
except Exception: #Exception é a maior classe dos erros, tratando qualquer erro
    print('ERRO DESCONHECIDO')