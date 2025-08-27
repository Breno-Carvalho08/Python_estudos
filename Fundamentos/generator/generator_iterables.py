#Generator expression, Iterables e Iterators em Python
    # iterable = ['Eu', 'Tenho', '__iter__']
    # iterator = iter(iterable)

    # lista = [numero for numero in range(10)] 
    # print(lista) #List comprehension - Acessar os indices

    # generator = (numero for numero in range(10))
    # print(generator) #Generator - Não tem indice nem tamanho

#Introdução e Generator function - Funções que sabem pausar a execução

#Ótimo para códigos que possuem alguma ordem
def generator(n = 0):
    yield 1 #Pausar - Todas as funções que tem o 'yield' são 'generator function'
    print('Continuando...')
    yield 2
    print('Continuando denovo')
    return 'ACABOU A BRINCADEIRA'
    

gen = generator(n = 0)
print(next(gen))
print(next(gen)) #Caso ocorra uma exceção, o 'return' será mostrado após a exceção (StopIteration: ACABOU A BRINCADEIRA)

#Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1 #Pausas
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10 #Pausas
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4 #Pausas
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
