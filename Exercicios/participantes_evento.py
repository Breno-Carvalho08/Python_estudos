workshop_python = {"Ana", "Carlos", "João", "Beatriz", "Lucas"}
curso_dados = {"Lucas", "Mariana", "Carlos", "Fernanda", "Paulo"}

#Total de pessoas que participaram do evento
total_pessoas = len(workshop_python | curso_dados)

#Pessoas que participaram dos dois
workshop_and_curso_dados = workshop_python & curso_dados

#Pessoas que participaram só do workshop
workshop_only = workshop_python - curso_dados

#Pessoas que participaram só do curso
curso_only = curso_dados - workshop_python 

escolha = int(input('[1] - Total de pessoas\n[2] - Participaram dos dois\n[3] - Participaram apenas do Workshop\n[4] - Participaram apenas do curso\n'))

while True:
    match escolha:
        case 0:
            break
        case 1:
            print(f'Total de pessoas: {total_pessoas}')
        case 2:
            print(f'Participaram dos dois: {workshop_and_curso_dados}')
        case 3:
            print(f'Apenas o Workshop: {workshop_only}')
        case 4:
            print(f'Apenas curso de dados: {curso_only}')
        case _:
            print('\n❌ Opção inválida. Por favor, escolha de 1 a 4.')
    