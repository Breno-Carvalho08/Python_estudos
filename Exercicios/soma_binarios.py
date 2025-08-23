

def tranformar_binario(numero):
    numero_binario = ''
    while numero != 0:
        digito_binario = numero % 2 
        numero = numero // 2
        numero_binario += str(digito_binario)
        
    return numero_binario[::-1]

def somar_binarios(num1, num2):
    valor_binario = num1 + num2
    numero_binario = ''
    while valor_binario != 0:
        digito_binario_1 = valor_binario % 2
        valor_binario = valor_binario // 2
        numero_binario += str(digito_binario_1)
    return numero_binario[::-1]

#Multiplicar e dividir binarios segue a mesma lógica
    
            

print(tranformar_binario(12))
print(somar_binarios(56,10))
