import json
import os

ARQUIVO = 'alunos.json'

def cadastrar_aluno(nome, serie_atual, nota):

    #Nomeamos o arquivo para facilitar sua busca 

    #Importamos a biblioteca 'os' e caso o arquivo exista ele lê o arquivo e carrega ele. Caso não, uma lista 'dados' é criada
    if os.path.exists(ARQUIVO):
        #É criado um cursor para que o arquivo seja lido
        with open(ARQUIVO, 'r', encoding='utf-8') as file:
            try:
                dados = json.load(file)
            except json.JSONDecodeError: #Caso o arquivo esteja vazio ou corrompido, evita erro e continua com lista vazia.
                dados = []
    else:
        dados = []

    novo_aluno = {
        'nome': nome,
        'ano': serie_atual,
        'nota': nota
    }

    dados.append(novo_aluno)

    #Cria um cursor para escrever no arquivo
    with open(ARQUIVO, 'w') as file: #Abre o arquivo em modo de escrita
        json.dump(dados, file, indent=4, ensure_ascii=False) #Salva a lista inteira (incluindo os anteriores e o novo).

    
def mostrar_alunos():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, 'r') as file: #Abrir o arquivo em modo de leitura
                lista_alunos = json.load(file) # Lê o conteudo do arquivo e transforma em um objeto python (no caso uma lista)

                for alunos in lista_alunos:
                    print(f'Nome: {alunos['nome']} | Ano: {alunos['ano']} | Nota: {alunos['nota']}')
        
        except json.JSONDecodeError:
            print("Arquivo vazio ou corrompido.")
            return
        
        

def excluir_aluno(nome, ano):
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, 'r') as file: #Abrir o arquivo em modo de leitura
                deletar_aluno = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo não encontrado ou vazio.")
            return
    nova_lista = []

    for aluno in deletar_aluno:
        #Caso o nome esteja na lista, ele passa para o próximo nome. Assim excluimos o nome, apenas não acrescentando ele na tabela 'nova_lista'
        if aluno['nome'] == nome and aluno['ano'] == ano:
            continue
        else:
            nova_lista.append(aluno)
    
    with open(ARQUIVO, 'w') as file:
        json.dump(nova_lista, file, indent = 4)
    print(f'Aluno {nome} deletado com sucesso')


while True:
        print("\nMenu:")
        print("1 - Cadastrar novo aluno")
        print("2 - Mostrar todos os alunos")
        print("3 - Deletar aluno")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            opcao_int = int(opcao)
        except ValueError:
            print('Nota inválida')

        match opcao_int:
            case 1:
                nome = input('Nome do aluno: ')
                ano = input('Ano do aluno: ')
                nota = input('Nota do aluno: ')

                try:
                    nota_float = float(nota)
                except ValueError:
                    print('Nota inválida')

                cadastrar_aluno(nome, ano, nota_float)
            case 2:
                mostrar_alunos()
            case 3:
                deletar_aluno = input('Nome do aluno: ')
                ano_aluno_deletar = input('Ano do aluno: ')

                excluir_aluno(deletar_aluno, ano_aluno_deletar)
            case 4:
                print('Saindo....')
                break




