#try, except, else e finally



a = 10
b = 0

try: 
    c = a / b
    print('1')
except ZeroDivisionError as divisao_zero: #Executado apenas na exceção
    print(divisao_zero.__class__.__name__)
else: 
    print('Será executado caso o código funcione sem erros')
finally: 
    print('Sempre será executado')