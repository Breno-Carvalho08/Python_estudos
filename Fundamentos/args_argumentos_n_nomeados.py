'''
args - Argumentos não nomeados
* ou *'args' (empacotamento e desempacotamento)

kwargs - Argumentos nomeados
'''

def soma(*args): #O 'args' empacota os valores passados como argumento da função em forma de tupla
    soma = 0
    for i in args:
        soma += i
    return soma

# (soma(1,2,3,4,5,6,)) #Ou seja, caso o print(args) fosse chamado, ele apareceria assim: (1,2,3,4,5,6)

soma1 = soma(1,2,3,4,5,6,7,8,9,10,11,12)
print(soma1)

numeros = 1,2,3,4,5,6,7,8
#print(soma(numeros)) #TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'. Está tentando soma 'int' com 'tuple'
print(soma(*numeros)) #Com o '*' a gente está desempacotando a variável numeros, tornando possível fazer a soma.

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#1,2,3,4,5,6 = argumentos não nomeados
#nome e qualquer = argumentos nomeados

pessoa = {
    'nome': 'Breno',
    'sobrenome': 'Carvalho'
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.80
}

pessoa_completa = {**pessoa, **dados_pessoa}

# mostrar_argumentos_nomeados(1,2,3,4,5,6, nome='Breno', qualquer='Carvalho')
mostrar_argumentos_nomeados(**pessoa_completa)