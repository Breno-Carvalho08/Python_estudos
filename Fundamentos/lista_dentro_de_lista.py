
salas = [
    
    ['Lucas', 'Breno', 'Carlos'],   #0 O primeiro for vai ler esses índices.
    ['Maria', 'Caio', 'Ariel'],     #1
    ['Guilherme', 'Ana', 'Raphael'] #2
    #O for de dentro vai ler os índices de cada lista dentro da outra lista.
]

for i, nomes in enumerate(salas):
    print(f'Sala {i + 1}:')
    for j, nomes in enumerate(salas):
        print(f'{salas[i][j]}\n', end='')


'''
salas = [
    ['Lucas', 'Breno', 'Carlos'],   #0
    ['Maria', 'Caio', 'Ariel'],     #1
    ['Guilherme', 'Ana', (10,20,30,40,50)] #2
]

print(salas[2][2][2]) 
'''