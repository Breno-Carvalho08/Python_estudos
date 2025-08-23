class main:
    pass

from produto import produto


while True:
    nome_produto = input('Produto: ')
    quant_produto = int(input('Quantidade: '))
    produto.adicionar_produto(nome_produto, quant_produto)
    produto.mostrar_estoque()
    nome_produto = input('Produto: ')
    produto_encontrado = produto.deletar_produto(nome_produto)
    if produto_encontrado:
        print(produto_encontrado)
    else:
        print(produto_encontrado)
    produto.mostrar_estoque()
    if quant_produto == 0:
        break