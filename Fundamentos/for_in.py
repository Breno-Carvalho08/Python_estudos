#For é utilziado quando sabemos o tamanho daquilo que vamos iterar.
import random 
texto = 'Breno'

novo_texto_criptografado = ''

#range (start, stop, step) => começo, parada, passo
#range sozinho é um método
#O ultimo valor dentro do range não entra
for i in range (0, len(texto)):

    if texto[i] == 'B':
        print('Esse nome tem a letra B')
        continue
    else:
        novo_texto_criptografado += f'{(random.randrange(1, 1000)):04X}{random.choice(texto)}'
        print(texto[i])
print(novo_texto_criptografado)
        
    