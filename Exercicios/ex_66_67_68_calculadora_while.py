# Calculadora While

continuar = True

while continuar:
    num1 = input('Informe o primeiro número: ')
    num2 = input('Informe o segundo número: ')
    operador = input('Informe o operador: (+-/*)')

    numeros_validos = None

    #Tratamento de possíveis erros 
    try:
        #Conversão para evitar que os valores inválidos
        num1_check = float(num1)
        num2_check = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None
    
    #Condição com base no valor digitado
    if numeros_validos is None:
        print('Informe valores válidos')
        continue

    op_validos = '+-/*'

    #Tratamento para operados inválidos ou mais de um
    if operador not in op_validos: #
        print('Selecione um operador válido')
        continue
    if len(operador) > 1:
        print('Informe apenas um operador.')
        continue

    #Escolha dos operadores
    match operador:
        case '+': 
            print(num1_check + num2_check)
        case '-':
            print(num1_check - num2_check)
        case '*':
            print(num1_check * num2_check)
        case '/':
            print(num1_check / num2_check)

        #Sair ou não do loop 
    escolha = input('Deseja parar? [S/N]').upper()
    if escolha == 'S':
        continuar = False
            
    