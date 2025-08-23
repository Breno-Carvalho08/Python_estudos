# Exercício - Adiando execução de funções
def soma(x, y):
   return x + y 


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5) #Esse valor fica guardado e pode ser utilizado depois
multiplica_por_dez = criar_funcao(multiplica, 10) #Esse valor fica guardado e pode ser utilizado depois

# print(soma_com_cinco) <function criar_funcao.<locals>.interna at 0x0000012D6768C0E0>
print(soma_com_cinco(20)) #Passamos o argumento para a função 'interna'
# print(multiplica_por_dez) <function criar_funcao.<locals>.interna at 0x00000218A1DEC180>
print(multiplica_por_dez(5)) #Passamos o argumento para a função 'interna'













# print(soma_com_cinco) #<generator object criar_funcao at 0x000001B41BD5A5A0>
# print(next(soma_com_cinco)) #TypeError: soma() missing 1 required positional argument: 'y'
#Aqui, a função é pausada no momento que passamos o 'x'. Mas quando avançamos, o argumento 'y' ainda não foi passado, surgindo o 'TypeError'

# try: 
#     numero_float = float(numero)
#     soma_com_cinco = criar_funcao(soma, 5, numero_float)
#     multiplica_por_dez = criar_funcao(multiplica, 10, numero_float)
#     print(next(soma_com_cinco)) #Precisamos dar o next, se não ele irá mostrar apenas o local da memória onde ele está armazenado
#     print(next(multiplica_por_dez))
# except (TypeError ,ValueError) as error:
#     print(error)
    