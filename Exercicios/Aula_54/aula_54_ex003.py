"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input('Primeiro nome: ').strip() #Retira os espaços do começo e do final
has_space = first_name.count(' ') #Conta os espaços

if has_space: #Substitui os espaços caso tenha no meio do nome
    first_name = first_name.replace(' ','') 

first_name_check = first_name.isalpha() #isalpha() só será verdadeiro se a variável 'first_name' não possuir espaços
len_name = len(first_name)
len_name_below_4 = len_name <= 4
len_name_between_5_6 = (len_name >=5) and (len_name <= 6)
len_name_longer_6 = len_name > 6



if first_name_check:
    if len_name <= 1:
        print('Digite um nome válido')
    elif len_name_below_4:
        print('Nome curto!')
    elif len_name_between_5_6:
        print('Nome normal!')
    elif len_name_longer_6:
        print('Nome grande!')
else:
    print('Nome inválido')
