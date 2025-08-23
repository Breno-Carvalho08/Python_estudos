nome = 'Luiz Fernando de Carvalho'
nome_sem_espaco = nome.replace(' ','')
tamahno_nome = len(nome_sem_espaco)

cont = 0
string_nome_alterado = ''

while cont < tamahno_nome:
    novo_caractere = ('*' + nome_sem_espaco[cont]) 
    string_nome_alterado += novo_caractere #Concatenamos as letras alteradas dentro do while
    cont += 1 

print(string_nome_alterado + '*')

