from itertools import groupby
from functools import reduce

produtos = [
    {"codigo": 101, "nome": "Arroz 5kg", "preco": 24.90, "quantidade_vendida": 120, "categoria": "Alimentos"},
    {"codigo": 102, "nome": "Feijão 1kg", "preco": 8.50, "quantidade_vendida": 95, "categoria": "Alimentos"},
    {"codigo": 103, "nome": "Macarrão 500g", "preco": 4.20, "quantidade_vendida": 150, "categoria": "Alimentos"},
    {"codigo": 104, "nome": "Óleo de soja 900ml", "preco": 6.70, "quantidade_vendida": 200, "categoria": "Alimentos"},
    {"codigo": 105, "nome": "Açúcar 1kg", "preco": 5.30, "quantidade_vendida": 110, "categoria": "Alimentos"},
    {"codigo": 201, "nome": "Detergente 500ml", "preco": 2.80, "quantidade_vendida": 180, "categoria": "Limpeza"},
    {"codigo": 202, "nome": "Sabão em pó 1kg", "preco": 12.50, "quantidade_vendida": 75, "categoria": "Limpeza"},
    {"codigo": 203, "nome": "Amaciante 2L", "preco": 15.90, "quantidade_vendida": 60, "categoria": "Limpeza"},
    {"codigo": 204, "nome": "Água sanitária 1L", "preco": 4.90, "quantidade_vendida": 130, "categoria": "Limpeza"},
    {"codigo": 301, "nome": "Shampoo 400ml", "preco": 18.70, "quantidade_vendida": 85, "categoria": "Higiene"},
    {"codigo": 302, "nome": "Condicionador 400ml", "preco": 19.50, "quantidade_vendida": 78, "categoria": "Higiene"},
    {"codigo": 303, "nome": "Sabonete", "preco": 3.20, "quantidade_vendida": 250, "categoria": "Higiene"},
    {"codigo": 304, "nome": "Pasta de dente", "preco": 7.40, "quantidade_vendida": 140, "categoria": "Higiene"},
    {"codigo": 401, "nome": "Refrigerante 2L", "preco": 9.90, "quantidade_vendida": 210, "categoria": "Bebidas"},
    {"codigo": 402, "nome": "Suco natural 1L", "preco": 6.80, "quantidade_vendida": 95, "categoria": "Bebidas"},
    {"codigo": 403, "nome": "Água mineral 500ml", "preco": 2.50, "quantidade_vendida": 300, "categoria": "Bebidas"},
    {"codigo": 404, "nome": "Cerveja lata 350ml", "preco": 4.60, "quantidade_vendida": 500, "categoria": "Bebidas"},
    {"codigo": 501, "nome": "Biscoito recheado", "preco": 3.90, "quantidade_vendida": 220, "categoria": "Snacks"},
    {"codigo": 502, "nome": "Chocolate barra 100g", "preco": 6.20, "quantidade_vendida": 160, "categoria": "Snacks"},
    {"codigo": 503, "nome": "Batata chips 100g", "preco": 7.80, "quantidade_vendida": 140, "categoria": "Snacks"},
    {"codigo": 504, "nome": "Amendoim torrado 200g", "preco": 8.40, "quantidade_vendida": 90, "categoria": "Snacks"},
]
def calculo_total_vendas_reduce(acumulador, lista):
    valor_acumulado = acumulador + (lista['preco'] * lista['quantidade_vendida'])
    return valor_acumulado 

total = reduce(calculo_total_vendas_reduce, produtos, 0)
total = reduce(lambda ac, p: ac + (p['preco'] * p['quantidade_vendida']), produtos, 0)
print(total)

def calculo_total_vendas(lista):
    total_vendas = 0
    for item in lista:
        valor_total = item['preco'] * item['quantidade_vendida']
        total_vendas += valor_total
    IR = 0.15
    ICMS = 0.09
    valor_impostos = ((total_vendas * IR) + (total_vendas * ICMS))
    total_vendas -= valor_impostos
    return f'R$ {total_vendas}'

def produtos_mais_procurados(lista):
    produtos = sorted(lista, key=lambda item:item['quantidade_vendida'], reverse=True)
    for produto in produtos:
        print(f'Nome: {produto['nome']} - Qtd: {produto['quantidade_vendida']}')

def produtos_categoria(lista):
    lista_categoria = groupby(lista, key=lambda item:item['categoria'])
    for categoria, produto in lista_categoria:
        print(categoria)
        for item in produto:
            print(f'Nome: {item['nome']} - Qtd: {item['quantidade_vendida']} - Preço: {item['preco']}')
        print()

def vendas_por_categoria(lista):
    lista_ = sorted(lista, key=lambda item:item['categoria'])
    lista_categoria = groupby(lista_, key=lambda item:item['categoria'])
    for categoria, produto in lista_categoria:
        print(categoria)
        venda_total = 0
        for item in produto:
            venda_categoria = item['preco'] * item['quantidade_vendida']
            venda_total += venda_categoria
        print(f'R$ {venda_total}')
        print()

