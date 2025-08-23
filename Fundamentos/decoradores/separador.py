import time

lista = [1, 'b', (9, 40), 5, [1, 2, 3, 4, 5], {'nome': 'Breno'}, True, 4.5423, 78.5423, 'Python', 'Código', False, 0.0003, (15,364,754)]
estoque = ['Arroz', 'Feijão', 'Carne', 'Suco', 'Chocolate']

def criador_de_funcoes(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        is_list(*args, **kwargs)
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f'Tempo da função: {fim - inicio:.4f} segundos')
        return resultado
    return wrapper

@criador_de_funcoes
def separador_tipos(lista):
    list_of_numbers = []
    list_of_joint = []
    list_of_strings = []
    list_of_bool = []
    for valor in lista:
        if isinstance(valor, bool):
            list_of_bool.append(valor)
        elif isinstance(valor, (int, float)):
            list_of_numbers.append(valor)
        elif isinstance(valor, (list, tuple, dict)):
            list_of_joint.append(valor)
        elif isinstance(valor, str):
            list_of_strings.append(valor)
        else:
            ...
    return list_of_bool, list_of_joint, list_of_numbers, list_of_strings

def is_list(lista):
    if not isinstance(lista, list):
        raise TypeError('Is not a list')

booleans, joints, numbers, strings = separador_tipos(lista)
print(booleans)
print(joints)
print(numbers)
print(strings)