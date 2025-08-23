#Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    opcoes = pergunta['Opções']
    
    for j, opcao in enumerate(opcoes): #Utilizamos a variável 'pergunta' que foi criada.
        print(f'{j}) {opcao}')

    resposta = input('Qual a sua resposta?')

    acertou = False
    resposta_int = None
    qtd_opcao = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcao:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
                
    if acertou:
        qtd_acertos += 1
    else: 
        print('Errou')
    
print(f'Você acertou {qtd_acertos} de {len(opcoes) - 1} perguntas')
        
    