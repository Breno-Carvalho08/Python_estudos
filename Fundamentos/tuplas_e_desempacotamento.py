'''
Introdução ao desempacotamento + tuplas
'''
#Desempacotamento
nomes = ['Breno', 'Lucas', 'Carlos']
#nome1, nome2, nome3 = nomes #Cada valor da lista foi atribuido a uma váriavel
nome1, *_ = nomes #Pegando o primeiro valor da lista apenas. O underline(_) é usando para indicar que esse valor não será utilizado.
print(nome1, _) #O 'resto' está armazenando a lista ['Lucas', 'Carlos']
_, nome2, *_ = nomes #Ignorando o primeiro valor, pegando o segundo e armazenando o terceiro.
print(nome2)



#Tuplas - Uma lista imutável - Uma lista sem colchetes
nomes = ('Breno', 'Lucas', 'Carlos') #Imutáveis
# nomes[1] = 'outro' -> Isso aqui já não seria possível nas tuplas
print(nomes)



