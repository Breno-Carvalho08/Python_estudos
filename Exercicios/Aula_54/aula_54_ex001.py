"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número: ')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
except:
    print('O valor digitado não é um número ou ele não é inteiro.')