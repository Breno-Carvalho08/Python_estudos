import random
estoque = []

class produto:
    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant
        self.num_produto = random.randint(10000, 99999)
    
    #Métodos get
    def getNome(self):
        return self.nome
    
    def getQuant(self):
        return self.quant
    
    def getNumProduto(self):
        return self.num_produto
    
    def add_quant(self, quant):
        self.quant += quant
    
    def adicionar_produto(nome, quant):
        for p in estoque:
            if p.nome == nome:  # ✅ acessando atributo diretamente
                p.add_quant(quant)
                return
        novo_produto = produto(nome, quant)
        estoque.append(novo_produto)

    def mostrar_estoque():
        for item in estoque:
            print(f'Nome: {item.nome} | Quantidade: {item.quant}')
        print()
    
    def deletar_produto(nome):
        for i, p in enumerate(estoque):
            if p.nome == nome:
                estoque.pop(i)
                return f'Produto {p.nome} deletado com sucesso'
        return 'Produto não encontrado'


        
    
    



    



        