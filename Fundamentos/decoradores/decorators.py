# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        print(*args)
        for arg in args: #Confere se o argumento passado é uma string
            e_string(arg)
        resultado = func(*args, **kwargs) 
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string) #Função decorada esperando ser chamada
invertida = inverte_string_checando_parametro('1a2b3c') #Função decorada chamada
print(invertida)