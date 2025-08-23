"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a #Apontando para um mesmo valor na memória
lista_b = lista_a.copy() #Atribui uma cópia da lista_a para a lista_b

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)