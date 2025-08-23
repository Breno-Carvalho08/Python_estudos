lista = ['Breno', 'Caio' ,'Maria', 'Lucas']
#lista_enumerada = enumerate(lista) - Não utiliza o enumerate atribuindo a uma variável

for indice, nome in enumerate(lista): #Enumera cada item da sua lista
    print(indice, nome)

print()

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)