
# Forma utilizando o for (sem list comprehension)
# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

numeros = [1, 2, 3, 4, 5]
multiplicacao = [(numero * 2) for numero in numeros] #Cria uma cópia da lista 'numeros'
divisao = [(numero / 2) for numero in numeros]
quadrado = [(numero ** 2) for numero in numeros]

numeros[0] = 11
print(numeros)
print(multiplicacao)