#Variáveis livres + nonlocal
'''
 nonlocal é usada dentro de funções aninhadas (funções dentro de outras funções) para indicar que uma variável 
 não pertence nem ao escopo local da função atual nem ao escopo global, 
 mas sim ao escopo da função externa mais próxima.
'''

#Função que lembra o valor de uma variável
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar = ''):
        nonlocal valor_final # está alterando o valor da variável de fora do escopo 'interna', a variável da função pai
        #Caso o valor fosse alterado sem o 'nonlocal' teriamos um erro, porque não conseguiriamos acessar essa variável
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)