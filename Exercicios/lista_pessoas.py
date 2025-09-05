from itertools import groupby

pessoas = [
    {"nome": "Henrique", "sexo": "M", "idade": 36},
    {"nome": "Carla", "sexo": "F", "idade": 19},
    {"nome": "Felipe", "sexo": "M", "idade": 27},
    {"nome": "Ana", "sexo": "F", "idade": 25},
    {"nome": "Diego", "sexo": "M", "idade": 42},
    {"nome": "Gabriela", "sexo": "F", "idade": 22},
    {"nome": "Elisa", "sexo": "F", "idade": 33},
    {"nome": "Bruno", "sexo": "M", "idade": 30},
]

def ordena_sexo(lista):
    return lista['sexo']

def ordenar_lista_ordem_alfabetica(lista):
    return sorted(lista, key=lambda nome:nome['nome'])

def ordenar_lista_por_idade(lista):
    return sorted(lista, key=lambda idade:idade['idade'])

def pessoa_sexo_feminino(lista):
    sexo_feminino = []
    for pessoa in lista:
        if pessoa['sexo'] == "F":
            sexo_feminino.append(dict(pessoa))
    return sexo_feminino

def pessoa_sexo_masculino(lista):
    sexo_masculino = []
    for pessoa in lista:
        if pessoa['sexo'] == "M":
            sexo_masculino.append(dict(pessoa))
    return sexo_masculino

def ordenar_menor_que_30(lista):
    pessoas_menos_30 = []
    for pessoa in lista:
        if pessoa['idade'] < 30:
            pessoas_menos_30.append(dict(pessoa))
    return pessoas_menos_30

def ordenar_maior_que_30(lista):
    pessoa_maior_30 = []
    for pessoa in lista:
        if pessoa['idade'] >= 30:
            pessoa_maior_30.append(dict(pessoa))
    return pessoa_maior_30
        
pessoa_maior_que_30 = ordenar_maior_que_30(pessoas)
pessoa_menor_que_30 = ordenar_menor_que_30(pessoas)
ordem_alfabetica = ordenar_lista_ordem_alfabetica(pessoas)
sexo_masculino = pessoa_sexo_masculino(pessoas)
sexo_feminino = pessoa_sexo_feminino(pessoas)
idade_crescente = ordenar_lista_por_idade(pessoas)

grupos_masculino = groupby(sexo_masculino, key=ordena_sexo)
grupos_feminino = groupby(sexo_feminino, key=ordena_sexo)

for idade in idade_crescente:
    print(idade)

# for chave, valor in grupos_masculino:
#     print(chave)
#     for nome in valor:
#         print(nome)

# for chave, valor in grupos_feminino:
#     print(chave)
#     for nome in valor:
#         print(nome)