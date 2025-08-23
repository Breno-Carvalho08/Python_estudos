numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#if no começo - mapeando
#if no final - filtro
novos_numeros = [numero for numero in numeros if numero > 3] #Filtro
impares = [numero for numero in numeros if numero % 2 != 0] #Filtro
pares = [numero for numero in numeros if numero % 2 == 0] #Filtro

outro_if = [(numero if numero != 6 else 600) for numero in pares] 

print(impares)
print(pares)
print(outro_if)