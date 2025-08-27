# List comprehension em Python
# é uma forma rápida para criar lista a partir de iteráveis

#Forma convencional
lista = []
for numero in range(10):
    lista.append(numero)

#print(list(range(1,20)))

#List comprehension
# lista = [5 for numero in range(10)]
# print(lista)
# lista = [1 for numero in range(10)]
# print(lista)
# lista = [numero for numero in range(10)]
# print(lista)
# lista = [numero * 2 for numero in range(10)]
# print(lista)
# lista = [numero // 2 for numero in range(10)]
# print(lista)
from functools import partial


#Mapeamento de dados em list comprehension - Transforma (talvez) os dados, mas mantém o mesmo tamanho da lista
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

def aumentar_preco(valor, porcentagem):
    return round(valor * porcentagem)

#Criando funções a partir de uma já criada (aumentar_rpeco)
aumentar_em_sete_porcento = partial(aumentar_preco, 1.07) 
aumentar_em_dez_porcento = partial(aumentar_preco, 1.1)
aumentar_em_doze_porcento = partial(aumentar_preco, 1.12)

#Mapeamento o 'if' vem antes do 'for'
novos_produtos_preco = [
    {**produto, 'preco': aumentar_em_sete_porcento(produto['preco'])}
    if produto['preco'] > 20 else {**produto} #Usado para mapeamento 
    for produto in produtos
]

print(*novos_produtos_preco, sep='\n')

#Filtro de dados em list comprehension - Fazer a seleção do que pode entrar na lista

#No filtro, o 'if' vai depois do 'for'
lista = [
        n # Isso é o que vai ser incluido na lista. Pode ser uma lista, uma tupla, um dicionário 
        for n in list(range(50)) 
        if n % 3 == 0
    ]
print(lista)

novos_produtos_preco = [
    {**produto, 'preco': aumentar_em_doze_porcento(produto['preco'])}
    if produto['preco'] > 20 else {**produto} #Usado para mapeamento 
    for produto in produtos
    if produto['preco'] > 20 and produto['preco'] > 10 #Filtro
]

print(*novos_produtos_preco, sep='\n')
