import os
estoque = ['Arroz', 'Feijão', 'Carne', 'Suco', 'Chocolate']
indices_estoque = []
carrinho = []
  
while True:
    try:
        escolha = input('[1] - Adicionar ao carrinho\n[2] - Tirar do carrinho\n[3] - Mostrar carrinho\n[4] - Finalizar Compra\nOpção: ')
        escolha_int = int(escolha)

        match escolha_int:

            #Adicionar ao carrinho
            case 1: 
                os.system('cls')
                #Mostra os produtos do estoque para o usuário selecionar
                for  i, itens in enumerate(estoque, start = 1):
                    indices_estoque.append(i - 1)
                    print(f'[{i}] - {itens}') 

                entrada = input('Qual produto deseja adicionar ao carrinho? ')

                try:
                    entrada_int = int(entrada) - 1 #O -1 é adicionado para acompanhar os índices da lista
                
                    if entrada_int in indices_estoque:
                        carrinho.append(estoque[entrada_int])   
                    else:
                        print('Produto não encontrado')
                except ValueError:
                    print('Valor não encontrado ou não é possível converte-lo')

            #Tirar do carrinho
            case 2:
                os.system('cls')
                #Mostra o carrinho para o usuário selecionar o índice para tirar do carrinho
                for i, itens in enumerate(carrinho, start = 1):
                    print(i, itens)

                entrada = input('Qual produto deseja retirar do carrinho? ')
                try:
                    entrada_int = int(entrada) - 1
                    del carrinho[entrada_int] #Retira do carrinho
                except ValueError:
                    print('Digite um valor numérico')
                except IndexError:
                    print('Não é possível deletar esse índice.')

            #Mostrar carrinho
            case 3:
                os.system('cls')
                for itens in carrinho:
                    print(itens)
            case 4: 
                break
    except:
         print('Valor não encontrado ou não é possível converte-lo')

