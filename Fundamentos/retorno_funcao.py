'''
Retorno de funções
'''

'''
def soma1(x, y):
    print(x + y)
res1 = soma1(4,4)
res2 = soma1(3,3)
print(res1 + res2) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# Como o print é um não valor (None), o erro 'NoneType' é dado pois não é possível somar não valores
'''

def soma(x,y):
    return x + y #A função retornando algo, o valor pode ser utilizado em uma variável para novas utilizações

resultado_1 = soma(4,5)
resultado_2 = soma(5,6)
print(resultado_1 + resultado_2)