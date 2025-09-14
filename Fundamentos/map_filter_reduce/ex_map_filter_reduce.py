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

#Map

# 1) Criar uma lista apenas com os nomes dos produtos
nome_produtos = list(map(lambda x:x['nome'], produtos)) 
# 2) Calcular o faturamento de cada produto (preço * quantidade_vendida)
faturamento_por_produto = list(map(lambda x:x['preco'] * x['quantidade_vendida'], produtos)) 
# 3) Criar uma lista com todos os preços em formato de string (ex: "R$ 10.00")
lista_precos_str = list(map(lambda x:str(x['preco']),produtos))
# 5) Lista com as categorias - Set não permite repetição
categorias = set(map(lambda x:x['categoria'],produtos))

#Filter

# 6) Filtrar apenas os produtos da categoria "Bebidas"
produtos_bebidas = filter(lambda x:x['categoria'] == 'Bebidas', produtos)
# 7) Filtrar produtos que venderam mais de 150 unidades
produtos_150_unidades = filter(lambda x:x['quantidade_vendida'] >= 150, produtos)
# 8) Filtrar produtos com preço menor que 10 reais
produtos_10_menos = filter(lambda x:x['preco'] < 10, produtos)

#Reduce

def produto_maior_venda(acumulador, x):
    if acumulador['quantidade_vendida'] > x['quantidade_vendida']:
        return acumulador
    else:
        return x

# 9) Calcular o faturamento total da loja
faturamento_loja = reduce(lambda acc, x:acc + (x['preco'] * x['quantidade_vendida']), produtos, 0)
# 10) Encontrar o produto mais vendido (comparando quantidade_vendida)
produtos_mais_vendidos = reduce(produto_maior_venda, produtos)
# 11)Soma das unidades vendidas
total_unidades = reduce(lambda acc,x: acc + x['quantidade_vendida'], produtos, 0)

# Desafios (map + filter + reduce)

# 12) Criar um ranking dos 5 produtos que mais faturaram
produtos_mais_faturados = sorted(
    map(lambda p: {'nome': p['nome'], 'faturamento': p['preco'] * p['quantidade_vendida']},produtos),
    key = lambda x: x['faturamento'],
    reverse=True
)[:5]

# 13) Calcular o faturamento total por categoria 
faturamento_categoria_snacks = reduce(
    lambda acc, fat: acc + (fat['preco'] * fat['quantidade_vendida']), 
    filter(lambda cat: cat['categoria'] == 'Snacks', produtos), 0
    )

faturamento_categoria_higiene = reduce(
    lambda acc, fat: acc + (fat['preco'] * fat['quantidade_vendida']),
    filter(lambda cat: cat['categoria'] == 'Higiene', produtos), 0
    )

faturamento_categoria_limpeza = reduce(
    lambda acc, fat: acc + (fat['preco'] * fat['quantidade_vendida']),
    filter(lambda cat: cat['categoria'] == 'Limpeza', produtos), 0
    )

faturamento_categoria_alimento = reduce(
    lambda acc, fat: acc + (fat['preco'] * fat['quantidade_vendida']),
    filter(lambda cat: cat['categoria'] == 'Alimento', produtos), 0  
    )

faturamento_categoria_bebida = reduce(
    lambda acc, fat: acc + (fat['preco'] * fat['quantidade_vendida']),
    filter(lambda cat: cat['categoria'] == 'Bebidas', produtos), 0
    )
    

# 14) Criar uma lista apenas com os nomes dos produtos acima da média de faturamento

media_faturamento = faturamento_loja / len(produtos)
acima_media = list(
    map(lambda p: p["nome"],
    filter(lambda p: p["preco"] * p["quantidade_vendida"] > media_faturamento, produtos))
    )
    
print(acima_media)









   
