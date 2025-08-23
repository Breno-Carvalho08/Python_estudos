#Escopo Global
x = 1
y = 9

# Global é uma má prática 
def escopo():
    #Escopo local
    global y #Definindo dentro da função que y é Global, ele pode ser alterado de dentro da função 'escopo'
    y = 11 #Alterou o 'y' de 9 para 11
    x = 12 #Aqui 'x' está dentro do escopo da função 'escopo'
    def outra_funcao():
        global x
        x = 326
        print(x)
    outra_funcao()
    print(x)

print(x)
print(y)
escopo()
print(x)
print(y)
#print(x) - Aqui ele não vai ser executado porque 'x' está dentro do escopo da função