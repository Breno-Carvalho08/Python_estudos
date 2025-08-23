
def parcelamento(parcelas):
    def valor(valor):
        if valor < 500:
            return f'Parcelas de R${valor / parcelas:.2f}'
        if valor > 1000 and valor <= 2000:
            valor *= 1.20
            return f'Parcelas de R${valor / parcelas:.2f}'
        if valor > 2000:
            valor *= 1.50
            return f'Parcelas de R${valor / parcelas:.2f}'
    return valor

parcelas_6_vezes = parcelamento(6)
parcelas_12_vezes = parcelamento(12)
parcelas_18_vezes = parcelamento(18)
            
print(parcelas_6_vezes(2000))
print(parcelas_12_vezes(5000))
