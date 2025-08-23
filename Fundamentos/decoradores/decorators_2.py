import time

def funcition_maker(func): #func = divisivel_por_3 
    def wrapper(*args, **kwargs): #(*args, **kwargs) = numero
        start = time.time()
        is_number(*args, **kwargs)
        resultado = func(*args, **kwargs)
        end = time.time()
        print(f"Tempo de execução: {end - start:.10f} segundos")
        return resultado
    return wrapper

@funcition_maker
def divisivel_por_3(numero):
    if numero % 3 == 0:
        return 'Divisível por 3'
    else:
        return 'Não divisível por 3'
    
def is_number(num):
    if not isinstance(num, (int, float)):
        raise TypeError('O valor que passou não é um inteiro')

# numero = funcition_maker(divisivel_por_3)
numero_divisivel = divisivel_por_3(4.5)
print(numero_divisivel)