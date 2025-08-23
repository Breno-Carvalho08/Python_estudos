frase = 'Breno Carvalho'.lower()

#teste = 'aaaaaoooo'

i = 0

#Atribuimos valores iniciais parasas váriaveis que vamos utilizar
mais_letras = 0
menos_letras = 0
letra_mais_apareceu = ''
letra_menos_apareceu = ''

while i < len(frase): #Quantidade de repetições indefinidas
    letra = frase[i]
    cont = frase.count(letra) #conta a letra

    #Atribuimos valores para que a comparação possa ser feita durante o while.
    if mais_letras == 0 and menos_letras == 0:
        mais_letras = cont
        menos_letras = cont
        letra_atual = frase[i]
        letra_mais_apareceu = letra_atual
        letra_menos_apareceu = letra_atual
    
    #Caso seja vazio (ou seja, tenha espaço) ele volta para o começo do while pelo 'continue'
    if letra == ' ':
        i += 1
        continue

    #Caso a letra apareça mais que o valor atribuido para comparação, ele será alterado nesse if
    if cont > mais_letras:
        mais_letras = cont
        letra_mais_apareceu = letra
    
    #Caso a letra apareça menos que o valor atribuido para comparação, ele será alterado nesse if
    if cont < menos_letras:
        menos_letras = cont
        letra_menos_apareceu = letra

    i += 1

print(f'{letra_mais_apareceu} = {mais_letras}')
print(f'{letra_menos_apareceu} = {menos_letras}')

   
