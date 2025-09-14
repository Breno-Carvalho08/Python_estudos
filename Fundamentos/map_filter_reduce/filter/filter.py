def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Banana', 'preco': 1},
    {'nome': 'Maçã', 'preco': 1.50},
    {'nome': 'Abacaxi', 'preco': 2}
]

def produtos_preco_maior(lista):
    produtos = []
    for preco in lista:
        if preco['preco'] > 1.4:
            produtos.append(preco)
    return produtos


#filter(Função + variável)
# novos_produtos_2 = [
#     {**produtos, 'preco': lambda a:a * 3}
#     if produtos > 0.5 else {**produtos}
#                     ]
novos_produtos = filter(lambda x:x['preco'] > 1.4, produtos)
print_iter(novos_produtos)
# print(novos_produtos_2)