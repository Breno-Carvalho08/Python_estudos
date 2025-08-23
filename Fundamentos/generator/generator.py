def parcelamento(valor, parcelas):
    if parcelas <= 6:
        yield valor / parcelas
    elif parcelas > 6 and parcelas <= 12:
        valor *= 1.20
        yield valor / parcelas
    else:
        valor *= 1.50
        yield valor / parcelas

print(parcelamento(5000, 12)) 
