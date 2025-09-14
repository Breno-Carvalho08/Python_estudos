from functools import reduce

lista = [6.5,8.7,9.6]
def validando_notas(*args):
    lista = []
    for nota in args:
        if not isinstance(nota, (float, int)):
            raise TypeError
        else:
            lista.append(nota)
    return lista
        

def soma_notas(acumulador, args):
    lista_notas = validando_notas(args)
    return  round(acumulador + args, 2)
    


print(validando_notas(5.6,6.7,8.7))

nota_final = reduce(soma_notas, lista, 0)
print(nota_final/len(lista))

