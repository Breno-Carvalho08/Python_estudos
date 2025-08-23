import json

saldo = 0

def consultar_produtos():
    with open('lista_supermercado.json', 'r', encoding='utf-8') as arquivo:
        lista_supermecado = json.load(arquivo)

    for categoria, produtos in lista_supermecado.items(): 
        print(categoria)
        for itens in produtos:
            print(f"Nome: {itens['nome']} | Preço: R$ {itens['preco']}")
        print()  

def adicionar_carrinho():
    global saldo
    nome_produto = input('Informe o nome do produto: ')

    #Aqui criamos uma variavel para receber a lista que está no arquivo json
    with open('lista_supermercado.json', 'r', encoding='utf-8') as arquivo:
        lista_supermecado = json.load(arquivo)
    
    #A mesma coisa aqui para podermos criar o carrinho, que nesse caso será uma lista vazia
    with open('carrinho.json', 'r') as arquivo:
        carrinho = json.load(arquivo)

    produto_encontrado = False

    for _, produtos in lista_supermecado.items(): 
        for nome in produtos:
            if nome_produto == nome['nome']:
                produto_encontrado = True
                carrinho.append({'nome': nome['nome'], 'preco': nome['preco']})
                       
    if produto_encontrado:
        print('Produto adicionado')
        try:
            with open('carrinho.json', 'w') as arquivo:
                json.dump(carrinho, arquivo, indent= 4, ensure_ascii=False)
        except:
            print('Não foi possível adicionar ao carrinho')
    else:
        print('Produto não encontrado')

def valor_final():
    global saldo
    with open('carrinho.json', 'r') as arquivo:
        carrinho = json.load(arquivo)
    
    for item in carrinho:
        print(f'Nome: {item['nome']} | Preço: R${item['preco']}')
        saldo += item['preco']
    print()
    print(f'Valor final: R${saldo}')

        

while True:
    print('Menu Compra')
    print('1 - Consultar produto')
    print('2 - Adicionar ao carrinho')
    print('3 - Valor final')
    print('4 - Sair')

    escolha = int(input('Qual opção: '))

    match escolha:
        case 1:
            consultar_produtos()
        case 2:
            adicionar_carrinho()
        case 3:
            valor_final()
        case 4:
            break