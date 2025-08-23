lista = [1, 'b', (9, 40), 5, [1, 2, 3, 4, 5], {'nome': 'Breno'}, True, 4.5423]


filtro = [
    i for i in lista
    if isinstance(i, (tuple, list)) #Vai colocar dentro da lista apenas valores 'tuple' e 'list'
    ]

print(filtro)