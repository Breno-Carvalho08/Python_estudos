from functools import partial

produtos = [
    {'nome': 'Banana', 'preco': 1},
    {'nome': 'Maçã', 'preco': 1.50},
    {'nome': 'Abacaxi', 'preco': 2}
    ]

def aumento_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

#Partial é uma função que recebe uma função e os argumentos para criar novas funções
aumentar_quinze_porcento = partial(aumento_porcentagem, 1.15) 
aumentar_doze_porcento = partial(aumento_porcentagem, 1.12)

def mudar_preco_produto(produto):
    return {**produto, 'preco': aumentar_quinze_porcento(produto['preco'])}

# novos_valores = [
#     {**p,'preco': aumentar_doze_porcento(p['preco'])} for p in produtos
# ]

#Recebe uma função e um iterável para fazer o mapeamento
novos_produtos = map(mudar_preco_produto, produtos)


vezes_tres = list(map(lambda x: x * 3, [1, 2, 3, 4]))
print(vezes_tres)


for produto in novos_produtos:
   print(f'{produto['nome']} - R$ {produto['preco']}')