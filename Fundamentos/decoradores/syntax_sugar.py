
#Função decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        print(args)
        for arg in args: #Confere se o argumento passado é uma string
            e_string(arg)
        resultado = func(*args, **kwargs) 
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao #Syntax Sugar - Usa a função 'criar_funcao' na função 'inverte_string'
def inverte_string(string):
    print(f'{inverte_string.__name__}') #A função 'inverte_string' passa a ser chamada de 'interna'
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('1a2b3c') #Função decorada chamada
print(invertida)