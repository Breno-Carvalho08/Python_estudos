#Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritório'
}

novo_dict = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'nome'
    
}

print(novo_dict)