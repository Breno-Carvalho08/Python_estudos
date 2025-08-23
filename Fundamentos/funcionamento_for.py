'''
Iterável -> str, range, etc. Elemento que pode te entregar uma coisa por vez
Iterador -> quem sabe entregar um valor por vez.
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

texto = iter('Breno') #Ele chama um iterador para esse elemento. O iterador que é quem sabe mostrar um elemento por vez. 
# Por isso ele é usado no for.
# O for solicita o iterador (__iter__() ou iter()) para o iterálvel (str, range, etc)
#O next() chama o próximo valor que estiver disponível dentro do iterador
print(texto.__next__()) #Disponível no iterador = B
print(texto.__next__()) #Disponível no iterador = r
print(texto.__next__()) #Disponível no iterador = e
print(texto.__next__()) #Disponível no iterador = n
print(texto.__next__()) #Disponível no iterador = o
#Ou podemos escrever print(next(texto)) 

#Demostrativo de como o for funciona utilizando o while
# texto2 = 'Carvalho'
# iterador = iter(texto2) #Busca o iterador do iterável. Ele quem consegue mostrar um valor por vez.


#while True:
#   try:
'''
        O for então, utilizando o iterador, armazena isso em uma váriavel, no caso a variável 'letra' e chama o método next()
        para ir mostrando as próximas letras utilizando o iterador.
        '''
#       letra = next(iterador) 
        
#       print(letra)
#    except StopIteration: #Tramamos uma exceção específica
'''
        Quando a sequência do iterável termina, ele lança um a exceção chamada StopIteration, que irá falar quando não tem mais elementos
        dentro do iterável. O for identifica isso e quando a exceção é lançada, ele para o laço.
        '''
#       break

#Resumindo tudo isso que fizemos com while no for
# for letra in texto2:
#     print(letra)

iterator = ['Breno', 'Lucas', 'Carlos']
iterable = iter(iterator)
print(next(iterable))
print(next(iterable))
print(next(iterable))
# print(next(iterable)) #Exceção StopIteration
# print(next(iterable))
# print(next(iterable))