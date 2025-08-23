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

#Mapeamento de dados em list comprehension - Transforma (talvez) os dados, mas mantém o mesmo tamanho da lista
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

#Mapeamento o 'if' vem antes do 'for'
novos_produtos_preco = [
    {**produto, 'preco': produto['preco'] * 1.07}
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
    {**produto, 'preco': produto['preco'] * 1.07}
    if produto['preco'] > 20 else {**produto} #Usado para mapeamento 
    for produto in produtos
    if produto['preco'] > 20 and produto['preco'] > 10 #Filtro
]

print(*novos_produtos_preco, sep='\n')
