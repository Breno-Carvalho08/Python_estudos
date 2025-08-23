#Métodos úteis dos dicionários Python

import copy
pessoa = {
    'nome': 'Breno',
    'sobrenome': 'Carvalho',
    'l1': [0, 1, 2, 3],
}


#DELETANDO OS ITENS
# print(pessoa.get('l2'), 'Não existe')
# nome = pessoa.pop('nome')
# print(pessoa)
# lista = pessoa.popitem() #Apaga o último termo da lista
# print(pessoa)


#ATUALIZANDO VALORES
# pessoa.update({'nome': 'Carlos','idade': 24})
# pessoa.update(nome='Lucas', idade=23)
# tupla = ('nome', 'Caio'), ('idade', 24)
# pessoa.update(tupla)
# print(pessoa)


# SHALLOW COPY E DEEP COPY 
# pessoa2 = pessoa #Aqui não está sendo feita uma cópia, apenas 'pessoa2' aponta para o mesmo dicionário que 'pessoa'
# pessoa2 = pessoa.copy() #Shallow copy: qualquer mudança em um dos objetos será também refletida no outro.
# pessoa3 = copy.deepcopy(pessoa) #Deep copy: qualquer modificação em um objeto, não será refletida no outro.
print(pessoa['l1'][1]) 
# pessoa['nome'] = 'Carlos' #Apenas o primeiro dicionário é alterado, não afetando os outros dicionários.
# print(pessoa)
# print(pessoa2)
# print(pessoa3)
'''
"No shallow copy, eu consigo alterar os dados imutáveis?"

Não. Dados imutáveis (como strings, inteiros, tuplas) não são alterados — qualquer “mudança” é, 
na verdade, uma substituição da referência. Por isso, quando você faz pessoa['nome'] = 'Carlos', 
só o dicionário original muda, as cópias mantêm 'Breno' (a não ser que compartilhem a mesma referência — 
o que não ocorre com imutáveis quando reatribuídos).
'''


# METODOS UTEIS
# pessoa.setdefault('idade', 18) #adiciona valor se a chave não existe
# print(pessoa['idade'])
# print(len(pessoa)) - Quantas chaves
# print(list(pessoa.keys())) - Iterável com as chaves
print(list(pessoa.values())) #- Iterável com os valores
print(list(pessoa.items())) #- Iterável com chave e valores

# for chave in pessoa.keys(): #For para as chaves do dicionário
#     print(chave)

# for valor in pessoa.values(): #For para os valores do dicionário
#     print(valor)

# for chave, valor in pessoa.items(): #For para chave e valor do dicionário
#     print(chave, valor)
