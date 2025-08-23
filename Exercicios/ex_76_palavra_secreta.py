import random
import os
lista_palavra_secreta = ['Armario','Cadeira','Mouse','Computador',]
palavra_secreta = random.choice(lista_palavra_secreta).lower()
letras_disponiveis = ''
tentativa = 0
#Remover os espaços da palavra
cont_espacos = palavra_secreta.count(' ')
if cont_espacos > 0:
    palavra_secreta = palavra_secreta.replace(' ','')


'''
    #Fazendo uma string com todas as letras da palavra
    if letras_disponiveis == '':
        cont = 0
        while cont < len(palavra_secreta):
            encontrar_letra = palavra_secreta[cont]
            if encontrar_letra in letras_disponiveis:
                cont += 1
                continue
            else:
                letras_disponiveis += palavra_secreta[cont]
                cont += 1
'''
while True:
    letra = input('\nChute uma letra: ').lower()
    tentativa += 1


    #Tratamento para ser digitado apenas letras
    if len(letra) > 1:
        print('Apenas letras, não palavras.')
        continue

    if letra in palavra_secreta:
        letras_disponiveis += letra

    #Lógica para mostrar a palavra certa ou manter os asteriscos escondendo a palavra
    palavra_formada = ''
    #O for pode percorrer o iterável(no caso uma string) e armazenar um valor de cada vez.
    for letra_secreta in palavra_secreta: #letra_secreta irá passar pelas letras de palavra_secreta
        if letra_secreta in letras_disponiveis: #Caso ela esteja nas letras_disponiveis será mostrada
           palavra_formada += letra_secreta    
        else: #Em caso de erro será mostrado o '*'.
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)


    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', tentativa)
        letras_acertadas = ''
        numero_tentativas = 0
        break
            
        