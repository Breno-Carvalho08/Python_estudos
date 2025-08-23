'''
Listas em python
Tipo list - Mutável (Diferente dos tipos imutáveis(int, float, string, bool))
Suporta vários valores de todos os tipos em uma mesma lista.
Conhecimentos reutilizáveis - indices e fatiamento (string para list)

Métodos úteis: append, insert, pop, del, clear, extend, + ...
  append -> adiciona um item no final da lista
  insert -> adiciona um item no índice escolhido - insert(0, 4) Informamos o índice que vamos colocar e o valor para o índice
  pop -> remove do final ou de um índice escolhido
  del -> apaga um índice
  clear -> limpa a lista
print(bool([])) -> falsy

Create Read Update Delete (CRUD) - Criar Ler Atualizar Deletar
'''
#CRUD
#Lista é interessante trabalhar no fim dela, adicionando valores ou tirando valores
lista_num = [10, 20, 30, 40]
lista_num2 = [50, 60, 70, 80]
lista_num3 = lista_num + lista_num2 #unir duas listas
lista_num4 = lista_num.extend(lista_num2) #Como o extend retorna um valor None (um não valor) não atribuimos ele a uma váriavel.
#Caso precisarmos mexer na lista_num, lista_num2 ... podemos fazer apenas o lista_num.extend(lista_num2), sem atribuir a uma váriavel.

lista_num.append(lista_num2) #Adicionando uma lista dentro de uma lista
print(lista_num)
lista_num[0] = 100 #Atualiza o valor na posição 0
print(lista_num)
lista_num.append(50) #Adiciona o valor no final da lista
print(lista_num)
del lista_num[0] #Deleta o valor no índice 0
print(lista_num)
lista_num.pop() #Remove o ultimo elemento da lista
print(lista_num)
lista_num.pop(3) #Passando o indice para o pop remover da lista
print(lista_num)
print(lista_num3)
lista_num.insert(5, 100) #Adicionando na posição 5 de lista o valor 100
print(lista_num)
print(lista_num4) #None

'''
lista = ['Breno', 'Lucas', 'Carlos']
print(lista)

lista.append('João') #Adiciona no final da lista
print(lista)
print(lista[1])
print(lista[3])

lista_combinada = [True, 'Breno', 1.54, [], 5, 'Luiz']
print(lista_combinada)
print(f'Posição 3: {lista_combinada[3]}')
print(lista_combinada[2])
print(lista_combinada[1])
print(lista_combinada[0])
lista_combinada[3] = 'Lucas'
print(f'Posição 3: {lista_combinada[3]}')
'''

