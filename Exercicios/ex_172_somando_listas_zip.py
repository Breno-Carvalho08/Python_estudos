"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]



def somando_listas_zip(l1, l2):
    return [a + b for a, b in zip(l1, l2)]

def somando_listas_ziplongest(l1,l2):
    return [a + b for a,b in zip_longest(l1, l2, fillvalue = 0)]


soma = somando_listas_zip(lista_a, lista_b)
soma_2 = somando_listas_ziplongest(lista_a, lista_b)
print(soma)
print(soma_2)



        