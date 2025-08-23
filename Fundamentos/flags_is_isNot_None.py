'''
Flag (Bandeira) Marcar um local
None = Não Valor
is e is not = é e não é (tipo, valor, identidade)
id = Identidade
'''

#Formato de código ruim para saber se passou pela condição.
condicao = True

if condicao:
    passou_no_if = True #Criar uma váriavel dentro da condição para saber se ela foi chamada. (RUIM)
    print('Faça algo')
else:
    print('Não faça algo')


#Forma correta de saber se passou pela condição
condicao = True
passou_no_if = None #Definir a váriavel fora do escopo da condição.

if condicao:
    passou_no_if = True #Flag (A bandeira da esse controle para saber se o programa passou pela condição)
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) #passou_no_if é None (se for None, não passou no if)
print(passou_no_if, passou_no_if is not None) #passou_no_if não é None (se não for None, passou no if)

#Podemos utilizar o debugger também.