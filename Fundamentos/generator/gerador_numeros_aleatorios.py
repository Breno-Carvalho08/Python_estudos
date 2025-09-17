import random

def print_iter(func):
    try:
        while True:
            print(next(func))
    except StopIteration:
        pass

def gerador_aleatorio(limite):
    cont = 0
    while cont <= limite:
        num = random.randrange(0, 10000)
        yield num
        cont += 1


print_iter(gerador_aleatorio(20))
