# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy
for produto in produtos:
    print(produto)

print()
# Primeira solução   
def acrescimo_dez_por_cento():
    novos_produtos = copy.deepcopy(produtos)

    for produto in novos_produtos:
        produto['preco'] = round(produto['preco'] * 1.10, 2)
        print(produto)
    
# Segunda solução
def ordenar_por_nome():
    produtos_ordenados_por_nome = copy.deepcopy(sorted(produtos, key=lambda p: p['nome'], reverse=True))

    for produto in produtos_ordenados_por_nome:
        print(produto)

#Terceira solução
def ordenar_por_preco():
    produtos_ordenados_por_preco = copy.deepcopy(sorted(produtos, key= lambda p: p['preco']))

    for produto in produtos_ordenados_por_preco:
        print(produto)


    
    
    