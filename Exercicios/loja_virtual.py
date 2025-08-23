import os

nome_cliente = ''
carrinho = []
valor_total = 0


produtos = [
    {'nome': 'Tênis', 'preco': 89.90},
    {'nome': 'Calça', 'preco': 119.90},
    {'nome': 'Blusa', 'preco': 99.90},
    {'nome': 'Chuteira', 'preco': 79.90},
    {'nome': 'Luvas', 'preco': 89.90},
    {'nome': 'Bicicleta', 'preco': 489.90}
]


def mostrar_produtos():
    for i, produto in enumerate(produtos):
        print(f'{i}) {produto['nome']} - R$:{produto['preco']:.2f}')

def mostrar_carrinho():
    for i, itens in enumerate(carrinho):
        print(f'{i}) {itens['nome']}')

def adicionar_ao_carrinho():
    global valor_total #Declarando a variável 'valor_total' como global para poder ser usada na função 'adicionar_ao_carrinho'
    escolha = input('Qual produto deseja adicionar? (Informe o número)\n')
    escolha_int = int(escolha)

    #Flag para encontrar produto na lista
    produto_encontrado = False
    
    for i, item in enumerate(produtos):
        if escolha_int == i: #Igualamos ao 'i' para checarmos se o 'escolha_int' está em um dos índices das listas.
            produto_encontrado = True
            nome_produto = item['nome']
            valor_produto = item['preco']
            break

    if produto_encontrado:
        print(f'{nome_produto} adicionado(a) ao carrinho!')
        carrinho.append({'nome': nome_produto, 'preco': valor_produto})
        print(carrinho)
        valor_total += valor_produto
        print(f'R$ {valor_total:.2f}')

    if not produto_encontrado:
        print('Produto não encontrado...')

def remover_produto_carrinho():
    global carrinho
    global valor_total
    mostrar_carrinho()
    escolha = input('Qual produto deseja remover do carrinho? (Informe o número)\n')
    escolha_int = int(escolha)

    for i, item in enumerate(carrinho):
        if escolha_int == i:
            carrinho.pop(i)
            valor_total -= item['preco']
            print(f'{valor_total:.2f}')
            print(f'"{item['nome']}" excluído.')
                                    
continuar_compra = True

while continuar_compra:
    escolha = input('[1] - Mostrar Produtos\n[2] - Adicionar ao carrinho\n[3] - Remover produto\n[4] - Mostrar carrinho\n[5] - Sair\n')
    escolha_int = int(escolha)

    if escolha_int == 5:
        continuar_compra = False

    match escolha_int:
        case 1:
            os.system('cls')
            mostrar_produtos()
        case 2:
            adicionar_ao_carrinho()
        case 3:
            os.system('cls')
            remover_produto_carrinho()
        case 4:
            os.system('cls')
            mostrar_carrinho()

    
