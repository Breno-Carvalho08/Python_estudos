from itertools import groupby


alunos = [
    {"nome": "Lucas", "idade": 21, "nota": 5.5, "curso": "Arquitetura", "cidade": "Recife", "matriculado": True},
    {"nome": "Carla", "idade": 19, "nota": 9.3, "curso": "Direito", "cidade": "Belo Horizonte", "matriculado": True},
    {"nome": "Igor", "idade": 22, "nota": 7.1, "curso": "Computação", "cidade": "Brasília", "matriculado": True},
    {"nome": "Fernanda", "idade": 23, "nota": 7.9, "curso": "Computação", "cidade": "Porto Alegre", "matriculado": True},
    {"nome": "Juliana", "idade": 19, "nota": 8.8, "curso": "Direito", "cidade": "Manaus", "matriculado": False},
    {"nome": "Daniel", "idade": 21, "nota": 5.8, "curso": "Arquitetura", "cidade": "Curitiba", "matriculado": False},
    {"nome": "Ana", "idade": 20, "nota": 8.5, "curso": "Engenharia", "cidade": "São Paulo", "matriculado": True},
    {"nome": "Gabriel", "idade": 24, "nota": 6.2, "curso": "Engenharia", "cidade": "Fortaleza", "matriculado": False},
    {"nome": "Helena", "idade": 20, "nota": 9.0, "curso": "Medicina", "cidade": "Salvador", "matriculado": True},
    {"nome": "Bruno", "idade": 22, "nota": 6.7, "curso": "Medicina", "cidade": "Rio de Janeiro", "matriculado": True},
    {"nome": "Ricardo", "idade": 25, "nota": 7.4, "curso": "Engenharia", "cidade": "Campinas", "matriculado": True},
    {"nome": "Mariana", "idade": 18, "nota": 9.5, "curso": None, "cidade": "Florianópolis", "matriculado": False},
    {"nome": "Sérgio", "idade": 26, "nota": 6.0, "curso": "Direito", "cidade": "Natal", "matriculado": True},
    {"nome": "Patrícia", "idade": 20, "nota": 7.8, "curso": None, "cidade": "Goiânia", "matriculado": True},
    {"nome": "Thiago", "idade": 27, "nota": 5.2, "curso": "Computação", "cidade": "Belém", "matriculado": False},
    {"nome": "Sofia", "idade": 22, "nota": 8.1, "curso": "Arquitetura", "cidade": "Fortaleza", "matriculado": True}
]
#nome - idade - nota - curso - cidade - matriculado


#Ordenar por curso
def listar_curso(lista):
    return lista['curso']  

def ordenar_por_curso(lista):
    
    aluno = []
    alunos_sem_curso = []
    for i in lista:
        if i['curso'] == None:
            alunos_sem_curso.append(i)
        else:
            aluno.append(i)
    alunos_agrupados = sorted(aluno, key=listar_curso)
    alunos_cursos = groupby(alunos_agrupados, key=listar_curso)
    return alunos_cursos

#Organizar por cidade
def organizar_alunos_cidade(lista):
    return lista['cidade']

def ordenar_por_cidade(lista):
    
    ordena_cidade = []
    for cidade in lista:
        if cidade['cidade'] == None:
            continue
        else:
            ordena_cidade.append(cidade)
    cidade_agrupados = sorted(ordena_cidade, key=organizar_alunos_cidade)
    aluno_cidade = groupby(cidade_agrupados, key=organizar_alunos_cidade)
    return aluno_cidade

#Conferindo as matrículas
def matriculado(lista):
    
    alunos_matriculados = []
    for aluno in lista:
        if aluno['matriculado'] == True:
            alunos_matriculados.append(aluno)
    return alunos_matriculados
            
#Conferindo as notas para passar no semestre
def aprovados(lista):
    
    alunos_aprovados = []
    for aluno in lista:
        if aluno['nota'] > 6:
            alunos_aprovados.append(aluno)
    return sorted(alunos_aprovados, key=lambda nota:nota['nota'], reverse=True)

#Conferir as notas
def maior_nota(lista):
    
    lista_alunos = matriculado(lista)
    notas = sorted(lista_alunos, key=lambda nota:nota['nota'], reverse=True)
    return notas

nota = maior_nota(alunos)
aluno_matriculado = matriculado(alunos)
alunos_cidade = ordenar_por_cidade(alunos)
alunos_cursos = ordenar_por_curso(alunos)
alunos_maior_nota = maior_nota(alunos)
aluno_aprovado = aprovados(alunos)

escolha = input('[1] - Alunos matriculados\n[2] - Cidade dos alunos\n[3] - Curso dos alunos\n[4] - Maior nota\n[5] - Alunos aprovados\n')
try:
    escolha_int = int(escolha)

    match escolha_int:
        case 1:
            for matricula in aluno_matriculado:
                print(f'Nome: {matricula['nome']} - Matricula: {matricula['matriculado']}')
        case 2:    
            for cidade, alunos in alunos_cidade:
                print(cidade)
                for nome in alunos:
                    print(f'Nome: {nome['nome']} - Curso: {nome['curso']}')
                print()
        case 3:
            for curso, aluno in alunos_cursos:
                print(curso)
                for nomes in aluno:
                    print(f'{nomes['nome']} - Idade: {nomes['idade']} - Nota: {nomes['nota']}')
                print()
        case 4:
            for nota in alunos_maior_nota:
                print(f'Nome: {nota['nome']} - Curso: {nota['curso']} - Nota: {nota['nota']}')
        case 5:
            for aprovado in aluno_aprovado:
                print(f'Nome: {aprovado['nome']} - Curso: {aprovado['curso']} - Nota: {aprovado['nota']}')
except (TypeError, ValueError, NameError) as error:
    print(error)

