'''
Exercício: Gerenciador de Participação em Atividades de uma Academia
'''

#Serviços que a academia oferece
musculacao = set(['Breno','Lucas','Caio','Carlos',])
yoga = set(['Breno','Lucas','Raphael','Bruno'])
natacao = set(['Breno','Carlos','Maria','Lucas'])

def cadastro_aluno(nome):
    print(f'Seja bem vindo, {nome}!')
    escolha = int(input('Cadastro em:\n[1] - Musculação\n[2] - Yoga\n[3] - Natação\n'))
    match escolha:
        case 1:
            if nome not in musculacao:
                musculacao.add(nome)
                print(musculacao)
            else:
                print('Aluno já cadastrado')
        case 2:
            if nome not in yoga:
                yoga.add(nome)
                print(yoga)
            else:
                print('Aluno já cadastrado')
        case 3:
            if nome not in natacao:
                natacao.add(nome)
                print(natacao)
            else:
                print('Aluno já cadastrado')

def remover_aluno(nome):
    print('Uma pena que queira sair de uma aula...')
    escolha = int(input('Sair de:\n[1] - Musculação\n[2] - Yoga\n[3] - Natação\n'))
    match escolha:
        case 1:
            if nome in musculacao:
                musculacao.discard(nome)
                print('Agradecemos sua participação')
            else:
                print('Nome não encontrado.')
        case 2:
            if nome in yoga:
                yoga.discard(nome)
                print('Agradecemos sua participação')             
            else:
                print('Nome não encontrado.')
        case 3:
            if nome in natacao:
                natacao.discard(nome)
                print('Agradecemos sua participação')              
            else:
                print('Nome não encontrado.')

def exibir_alunos_att():
    escolha = int(input('Aulas:\n[1] - Musculação\n[2] - Yoga\n[3] - Natação\n'))
    match escolha:
        case 1:
            for nomes in musculacao:
                print(nomes)
        case 2:
            for nomes in yoga:
                print(nomes)
        case 3:
            for nomes in natacao:
                print(nomes)

def consultas():
    escolha = input('[1] - Fazem todas as atividades\n[2] - Fazem apenas uma atividade\n[3] - Fazem mais de uma atividade\n[4] - Total de alunos\n')
    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        match escolha_int:
            case 1:
                todas_att = musculacao & yoga & natacao
                todas_att_list = list(todas_att)
                for aluno_em_todas in todas_att_list:
                    print(aluno_em_todas,end=" ")
                    print()
            case 2:
                musculacao_apenas = musculacao - (yoga | natacao)
                yoga_apenas = yoga - (musculacao | natacao)
                natacao_apenas = natacao - (musculacao | yoga)
                print(f'Só musculação: {musculacao_apenas}\nSó yoga: {yoga_apenas}\nSó natação: {natacao_apenas}')
            case 3:
                # Alunos que fazem mais de uma atividade
                musculacao_e_yoga = (musculacao & yoga) 
                musculacao_e_natacao = (musculacao & natacao) 
                yoga_e_natacao = (yoga & natacao) 
                print(f'Musculação e yoga: {musculacao_e_yoga}\nMusculação e natação: {musculacao_e_natacao}\nYoga e natação: {yoga_e_natacao}')

            case 4:
                total_alunos = len(musculacao | yoga | natacao)
                print(f'Total de alunos: {total_alunos} alunos')

while True: 
    escolha = input('[1] - Cadastrar aluno\n[2] - Remover aluno\n[3] - Mostrar alunos\n[4] - Consultas\n[5] - Sair\n')

    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)

    if not escolha.isdigit():
        print('Por favor, digite um número válido.')
        continue
    
    if escolha_int:
        match escolha_int:
            case 1:
                nome = input('Informe o nome do aluno: ').strip().title()
                cadastro_aluno(nome)
            case 2:              
                nome = input('Informe o nome do aluno: ').strip().title()
                remover_aluno(nome)
            case 3: 
                exibir_alunos_att()
            case 4:
                consultas()
            case 5: 
                print('Agradecemos sua presença!')
                break
            case _:
                print('Informe uma opção válida')
    