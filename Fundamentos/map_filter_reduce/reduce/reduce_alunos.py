from functools import reduce
alunos = [
    {'nome': 'Breno', 'nota': [7.6,8.9,5.7]},
    {'nome': 'Lucas', 'nota': [5.3,8.9,2.4]},
    {'nome': 'Carlos', 'nota':[6.5,8.9,4.5]},
    {'nome': 'Ariel', 'nota': [3.5,6,8]},
    {'nome': 'Caio', 'nota':  [10,6.7,8.9]},
]
lista = [7.6,8.9,5.7,5.3,8.9,2.4,6.5,8.9,4.5]

def soma_notas(acumulador, nota):
    return acumulador + nota

soma = reduce(soma_notas, lista, 0)
media = soma / len(lista)

print(round(soma,3), round(media,2))


