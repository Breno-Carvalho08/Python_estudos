lista = [['Luiz','Luciane'],'Breno','Lucas','Raphael','Maria','Caio','Carlos']
tupla = 'Python','aprender','curso'

print(*lista)
print(*tupla)

a, *_, c = lista #Desempacotamento (*_ -> indica uma váriavel que provavelmente não será usada, como se estivesse pegando o resto da lista)
print(a,c)
print(_) #Todos os outros nomes ficaram armazenados dentro dessa variável

print(lista[0][0][0])

'''
for nome in lista:
    #print(nome)
    for letra in nome:
        print(letra)
'''
    