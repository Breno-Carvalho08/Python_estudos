
# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
def saudacao(msg, *nomes):
    return f'{msg}, {nomes}'

# Higher Order Functions - Funções que podem receber e/ou retornar outras funções
def executa(funcao, *parametro):
    return funcao(*parametro)

func_executa = executa(saudacao, f"Olá, Breno, Lucas, Maria, Raphael")
print(func_executa)