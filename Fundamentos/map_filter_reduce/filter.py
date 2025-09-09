def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Banana', 'preco': 1},
    {'nome': 'Maçã', 'preco': 1.50},
    {'nome': 'Abacaxi', 'preco': 2}
]

#filter(Função + variável)
novos_produtos_2 = [
    {**produtos, 'preco': lambda a:a * 3}
    if produtos['preco'] > 0.5 else {**produtos}
                    ]
novos_produtos = filter(lambda p:p['preco'] > 1.4, produtos)
print_iter(novos_produtos)
print(novos_produtos_2)