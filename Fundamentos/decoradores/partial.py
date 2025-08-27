#Partial é um jeito mais simples de utilizar os decoradores e criar novas funções

from functools import partial

produtos = [
    {'nome': 'Banana', 'preco': 1},
    {'nome': 'Maçã', 'preco': 1.50},
    {'nome': 'Abacaxi', 'preco': 2}
    ]

def aumento_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

#Partial é uma função que recebe uma função e os argumentos para criar novas funções
aumentar_dez_porcento = partial(aumento_porcentagem, 1.1) 
aumentar_doze_porcento = partial(aumento_porcentagem, 1.12)

novos_valores = [
    {**p,'preco': aumentar_doze_porcento(p['preco'])} for p in produtos
]


for produto in novos_valores:
    print(f'{produto['nome']} - R$ {produto['preco']}')