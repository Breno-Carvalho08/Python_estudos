lista_pessoas = []

def registrar_pessoas(**kwargs):
    lista_pessoas.append({**kwargs})

def mostrar_pessoas(lista):
    for pessoa in lista:
        print(pessoa)


while True:
    
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    idade = input('Idade: ')
    try:
        if idade.isdigit():
            idade_int = int(idade)
            registrar_pessoas(nome = nome, sobrenome = sobrenome, idade = idade_int)
            mostrar_pessoas(lista_pessoas)
    except ValueError:
        print('Valor inválido')