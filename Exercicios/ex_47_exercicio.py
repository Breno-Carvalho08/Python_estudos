nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

#nome_invertido = nome[::-1]
#espaco_nome = nome.count(' ')
nome_sem_espaco = nome.replace(' ','')
#tamanho_nome = len(nome)

#print(nome_sem_espaco.isalpha())


if (nome_sem_espaco.isalpha() and nome != '') and (idade.isnumeric() and idade != ''):
    int_idade = int(idade)
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é { nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaço(s)')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'Primeira letra do nome {nome[0]}')
    print(f'Ultima letra do nome é {nome[len(nome) - 1]}')
else:
    print('Você deixou campos vazios.')
    
