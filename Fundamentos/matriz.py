#Para criar matrizess, o for é mais interessante que o while

for linha in range(1,8):
    for coluna in range(1,8):
        #Imprime o elemento atual e, usando o parâmetro end=" ", adiciona um espaço em branco no final da impressão, ao invés de uma quebra de linha.
        print(f'[{linha}, {coluna}]', end='  ') 
    print()
