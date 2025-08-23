#Função Lambda 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# #Essa função foi criada unicamente para ensinar ao python como fazer a ordenação
# def ordenar(item):
#     return item['nome'] #Nesse caso, falamos para o python que queremos que seja ordenado pelo nome.
# como '.sort' não faz ordenação com dicionários, temos que mostrar qual o parâmetro para ordenar (o primeiro nome) 

# def exibir(lista):
#     for item in lista:
#         print(item)

# l1 = sorted(lista, key= lambda item: item['nome'])#Utilizando a função lambda
# l2 = sorted(lista, key= lambda item: item['sobrenome'])

# exibir(l1)
# print()
# exibir(l2)

#Função Lambda mais complexa

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

#MÁ PRÁTICA
#funcao = lambda parametro : parametro 

#Lambda é para ser algo fácil, se começa a ficar complexo, está errado

#Função lambda não tem nome e nem parentêses
print(executa(lambda x, y: x + y, 2, 3), executa(soma, 2, 3), soma(2,3))

