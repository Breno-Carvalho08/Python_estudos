produtos = [
    {"Arroz": 25.90},
    {"Feijão": 8.50},
    {"Macarrão": 4.20},
    {"Carne": 42.75},
    {"Leite": 6.30},
    {"Pão": 9.80},
    {"Queijo": 19.90},
    {"Café": 17.40},
    {"Óleo": 7.60},
    {"Chocolate": 12.50}
]

#Lista com dicionários pode ser ordenada por nome ou preço utilizando sorted e lambda()
def ordenar_por_nome(lista):
    return sorted(lista, key=lambda produto: list(produto.keys()))

def ordenar_por_preco(lista):
    return sorted(lista, key=lambda produto: list(produto.values()))

lista_ordenada_por_nome = ordenar_por_nome(produtos)

for produtos in lista_ordenada_por_nome:
    for nome, preco in produtos.items():
        print(f'{nome}: R$ {preco:.2f}')








