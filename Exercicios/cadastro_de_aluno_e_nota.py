media_aluno = 0
media_aluno_final = 0
media_sala = 0
total_notas = 0

lista_de_alunos = [
    {'nome': 'Breno', 'notas':[10, 6.5, 5.7]},
    {'nome': 'Ana', 'notas':[5.5, 4.6, 9.4]},
    {'nome': 'Lucas', 'notas':[7.7, 8.9, 5.5]}
]


#Fazendo a contagem de quantas notas foram digitadas para fazer a média
for i in lista_de_alunos:
    notas = i['notas']

for indice in lista_de_alunos:
    for j in indice['notas']:
        total_notas += 1
        media_sala += j

validar_aluno = input('Digite o nome do aluno: ')

try:
    validar_aluno_str = validar_aluno.isalpha()
    #Flag criada
    aluno_cadastrado = False

    if validar_aluno_str:
        for nome in lista_de_alunos:
            if validar_aluno in nome['nome']:
                aluno_cadastrado = True
                break

        if aluno_cadastrado:
            for nota in nome['notas']:
                media_aluno += nota

            media_aluno_final = media_aluno/len(notas)   
            media_sala_final = media_sala/total_notas
            if media_aluno_final < media_sala_final:
                print('Tem que se dedicar melhor aos estudos.')
            else:
                print('Parabéns, você está acima da média!')

            print(f'Aluno: {validar_aluno}\nMédia final: {media_aluno_final:.2f}')
            print(f'Média da sala: {media_sala_final:.2f}')

          

        if not aluno_cadastrado:
            print('Aluno não encontrado')
            cadastrar_aluno = input('Nome do aluno: ')
            entrada = input('Informe as notas do aluno(a) (separe as notas por espaços): ')
            notas_aluno = list(map(float, entrada.split()))
            lista_de_alunos.append({'nome': cadastrar_aluno, 'notas':notas_aluno})

            for nota in notas_aluno:
                media_aluno += nota

            media_aluno_final = media_aluno/len(notas)   
            media_sala_final = media_sala/total_notas
            if media_aluno_final < media_sala_final:
                print('Tem que se dedicar melhor aos estudos.')
            else:
                print('Parabéns, você está acima da média!')

            print(f'Aluno: {validar_aluno}\nMédia final: {media_aluno_final:.2f}')
            print(f'Média da sala: {media_sala_final:.2f}')
            
except TypeError:
    print('Valor inválido')


