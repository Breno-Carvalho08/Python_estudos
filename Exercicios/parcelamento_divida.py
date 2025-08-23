import datetime

cliente_saldos_negativos = 0

clientes = {
    "Ana Souza": -1520.75,
    "Bruno Lima": -874.30,
    "Carla Mendes": -2350.00,
    "Diego Rocha": 410.90,
    "Eduarda Nunes": -3025.50,
    "Felipe Tavares": 127.35,
    "Gustavo Alves": -986.60,
    "Helena Martins": 10.00,
    "Igor Ferreira": -780.25,
    "Juliana Ramos": 194.10
}

def menu_consulta(nome):
    if nome in clientes.keys():
        hora = datetime.datetime.now().hour
        if hora > 6 and hora <= 12:
            escolha = int(input(f'Bom dia senhor(a) {nome}, o que deseja fazer?\n[1] - Regularizar nome\n[2] - Sair\n'))
            match escolha:
                case 1:
                    regularizar_nome(nome)
                case 2:
                    print('Obrigado.')
            
        if hora > 12 and hora < 19:
            escolha = int(input(f'Boa tarde senhor(a) {nome}, o que deseja fazer?\n[1] - Regularizar nome\n[2] - Sair\n'))
            match escolha:
                case 1:
                    regularizar_nome(nome)
                case 2:
                    print('Obrigado.')
                    
        if hora > 19:
            escolha = int(input(f'Boa noite senhor(a) {nome}, o que deseja fazer?\n[1] - Regularizar nome\n[2] - Sair\n'))
            match escolha:
                case 1:
                    regularizar_nome(nome)
                case 2:
                    print('Obrigado.')

def consultar_saldos_negativos():
    global cliente_saldos_negativos
    for saldo in clientes.values():
        if saldo < 0:
            cliente_saldos_negativos += 1
    print(f'Temos {cliente_saldos_negativos} pessoas com saldo negativo em nosso sistema.')

def mostrar_pessoas_com_saldo_negativo():
    for nome, saldo in clientes.items():
         if saldo < 0:
            print(f'{nome}: R${saldo}')

def pagamento_parcelado(numero_parcelas, saldo):
    if numero_parcelas <= 12:
        print(f'R${-(saldo/numero_parcelas):.2f} em {numero_parcelas}X')

    if numero_parcelas > 12 and numero_parcelas <= 24:
        print(print(f'R${(-(saldo*1.20)/numero_parcelas):.2f} em {numero_parcelas}X'))

    if numero_parcelas > 24:
        print(f'R${(-(saldo*1.40)/numero_parcelas):.2f} em {numero_parcelas}X')  

def pagamento_a_vista(valor_a_vista, nome):
    if valor_a_vista > 0:
        saldo += valor_a_vista
        clientes[nome] = saldo 
        print(f'{nome}, {saldo:.2f}')
    else:
        print('Valor inválido')

def regularizar_nome(nome):
    if nome in clientes:
        saldo = clientes[nome]
        if saldo < 0:
            print(nome, saldo)
            escolha = input('Como dejesa pagar as pendências\n[1] - Á Vista\n[2] - Parcelado\n')
            escolha_int = int(escolha)
            match escolha_int:
                case 1:
                    valor_para_quitar_a_vista = float(input(f'Deposite o valor R${-(saldo)} para quitar a divida:'))
                    pagamento_a_vista(valor_para_quitar_a_vista, nome)
                case 2:
                    numero_parcelas = int(input('Quantas parcelas (meses): '))
                    pagamento_parcelado(numero_parcelas, saldo)
        else: 
            print('Você não está negativo, não tem nada pendente.')        
        
nome_consulta = input('Informe seu nome para que possamos fazer a consulta: ')
menu_consulta(nome_consulta)

