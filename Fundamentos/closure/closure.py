'''
Closure e funções que retornam outras funções

Closure é uma função que lembra das variáveis do ambiente onde foi criada, mesmo depois desse ambiente ter sido encerrado.
'''

def criar_saudacao(saudacao): # é uma função externa que recebe o nome de alguém.
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # criar_saudacao retorna a função saudar, sem executá-la.
    #Salva o valor da função na memória e lembra o valor atribuido a ela


saudacao_bom_dia = criar_saudacao('Bom dia')
saudacao_boa_noite = criar_saudacao('Boa noite')
print(saudacao_bom_dia) #é a forma como o Python mostra que você está lidando com um objeto função, e informa onde ele está na memória.
print(saudacao_bom_dia('Breno')) #Aqui a função é executada e o valor atribuido os parâmetros são lembrados
print(saudacao_boa_noite('Breno')) #Mandamos o valor para a função 'saudar'

for nome in ['Lucas', 'Maria', 'Carlos']:
    print(saudacao_bom_dia(nome))

