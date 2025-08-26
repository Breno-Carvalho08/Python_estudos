#Combinação - Ordem não importa - iterável + tamanho do grupo
#Permutação - Ordem importa
#Produto - Ordem importa e repeta valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['Breno', 'Carlos', 'Luiz', 'Caio']
camisetas = [['Preta','Branca', 'Azul', 'Vermelho'], 
             ['P', 'M','G'], 
             ['Masculino', 'Feminino']]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))