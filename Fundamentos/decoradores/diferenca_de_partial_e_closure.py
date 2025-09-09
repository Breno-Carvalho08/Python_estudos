from functools import partial

#Forma de criar uma função decoradora utilizadno partial
def multipicador(numero, multiplica):
    return numero * multiplica

multiplicar_por_dois = partial(multipicador, 2)
multiplicar_por_tres = partial(multipicador, 3)
print('PARTIAL')
print(multiplicar_por_dois(5))
print(multiplicar_por_tres(5))

print()

#Forma de criar uma função decoradora utilizando closure
def decorador(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

entrada = int(input('Numero:'))
decoradora = decorador(multipicador)
multiplicar_por_cinco = decoradora(entrada,5)
multiplicar_por_dez = decoradora(entrada,8)
print('CLOSURE')
print(multiplicar_por_cinco)
print(multiplicar_por_dez)






