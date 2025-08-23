def multiplicacao(*args):
    valor_final = 1
    for i in args:
        valor_final *= i
    return valor_final

def par_impar(numero):
    try:
        numero_int = int(numero)
    
        if numero_int  % 2 == 0:
            return f'{numero_int } é Par'
        return f'{numero_int } é Ímpar'
    except ValueError:
        return 'valor digitado não é um número'

resultado = multiplicacao(1,2,3,4,5,6,7,8,9,10)
resultado2 = par_impar(4)
print(resultado)
print(resultado2)