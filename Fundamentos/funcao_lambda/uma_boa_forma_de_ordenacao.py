alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.2},
    {"nome": "Carla", "nota": 9.1},
    {"nome": "Diego", "nota": 6.8},
    {"nome": "Eduarda", "nota": 8.0},
    {"nome": "Felipe", "nota": 5.9},
    {"nome": "Gabriela", "nota": 7.7},
    {"nome": "Henrique", "nota": 9.4},
    {"nome": "Isabela", "nota": 6.3},
    {"nome": "João", "nota": 8.9}
]

def aluno_ordem_alfabetica(lista):
    return sorted(lista, key=lambda valor: list(valor.keys()))

def aluno_ordem_por_nota(lista):
    return sorted(lista, key=lambda valor: list(valor.values()),reverse=True)

lista_ordenada_por_nome = aluno_ordem_alfabetica(alunos)
lista_ordenada_por_nota = aluno_ordem_por_nota(alunos)

print(lista_ordenada_por_nome)

