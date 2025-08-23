#Sets - Conjuntoos em python
#Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

# s1 = set('Breno') #Parecem dicionários - Pode não garantir a ordem - Vai iterar sobre o valor 
# s2 = {'Breno', 1, 3, 4}

#Sets são eficientes para remover valores duplicados de iteráveis
# - Seus valores serão sempre únicos
# - Não aceitam valores mutáveis (listas, dicionários)
# - Não tem índexes
# - Não garantem ordem
# - São iteráveis (for, in, not)
# s1 = {1,1,1,2,2,3,4,5,5,6}

#Passo para remover valores repitidos em uma Lista utilizando o Set
# l1 = [1,2,2,3,3,4,4,4,4,5,6]
# print(l1)
# s1 = set(l1)
# l2 = list(s1)
# # s2 = {1,2,3,{1,2,3}}
# s2 = {1,'Lucas',6.5, 'Breno',111}
# print('Lucas' in s2) #Iterável com 'in'
# print(l2)

#Métodos úteis em python: add, update, clear, discard
# s1 = set()
# s1.add('Breno') # Só aceita um valor por vez
# # s1.update('Lucas') #Adiciona no set, mas de forma iterada (letra por letra) - Utilizado para mandar vários valores também
# s1.update(('Breno',5,6,7,'Carlos')) #Tupla
# #s1.clear() - Limpa o set por completo
# s1.discard('Carlos') # Passamos o valor que queremos eliminar
# print(s1)

#Operadores úteis:
#união |
#intersecção & - Item presente em ambos
#diferença (-) - Itens presentes apenas no set da esquerda 
#diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# #União
# s3 = s1 | s2
# print(s3) # sem valores duplicados

# #Intersecção
# s3 = s1 & s2
# print(s3) #Presente nos dois

# #Diferença
# s3 = s1 - s2 
# print(s3) #irá mostrar o item que está apenas no lado esquerdo

# #Diferença simétrica
# s3 = s1 ^ s2
# print(s3) # o valor 1 não está presente em s2 e o valor 4 não está presente em s1

# s1 = {'Breno', 'Carlos','Lucas'}
# s2 = {'Ariel', 'Breno','Carlos','Caio'}

# s3 = s1 | s2
# print(s3)

# s3 = s1 & s2
# print(s3)

# s3 = s1 - s2
# print(s3) #Apenas o 'Lucas' está do lado esquerdo
# s3 = s2 - s1
# print(s3) #O 'Ariel' e o 'Caio' estão apenas do lado esquerdo

# s3 = s1 ^ s2
# print(s3) #Valores presentes apenas em um dos dois

#Exemplo
letras = set()
while True:
    letra = input('Digite: ')
    
    if letra not in letras:
        letras.add(letra)
        print(letras)
    else:
        print('Letra já digitada')