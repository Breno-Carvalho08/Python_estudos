'''
Dicionários em Python - Tipo "chave" e "valor"
'''

# pessoa = {
#     'nome': 'Breno',
#     'sobrenome': 'Carvalho',
#     'idade': 18,
#     'altura': 1.8,
#     'endereco': [{'Av': 'Orlando Angelo Gastaldo', 'número': 90}]
# }

# for chave in pessoa:
#     print(chave, pessoa[chave])

# print()

# pessoa['peso'] = 85 #Criando um atributo para o nosso dicionário

# if pessoa.get('trabalho') is None: #Recurso utilizado pelo dicionário para sabermos se esse atributo existe.
#     print('Trabalho não existe')
# else:
#     print('Trabalho existe')
# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

#Empacotamento e desempacotamento em dicionários

pessoa = {
    'nome': 'Breno',
    'sobrenome': 'Carvalho'
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.80
}

# (chave, nome), (valor, sobrenome) = pessoa.items()
# print(chave, nome, valor, sobrenome)

# for chave, valor in pessoa.items():
#     print(valor)

#Desempacotamento de um dicionário em outro dicionário vazio
pessoa_completa = {**pessoa, **dados_pessoa} #Adicionando outros valores a um dicionário vazio
print(pessoa_completa)
