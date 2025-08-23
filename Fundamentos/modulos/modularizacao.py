# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import modularizacao_m #Caso não seja o primeiro a ser executado, ele recebe o nome do módulo (modularizacao_m)
import modulos
from modulos import soma
try:
    import sys
    sys.path.append('/Users/Breca/Desktop') #Importamos um módulo de outro local, um que não está na mesma pasta
except ModuleNotFoundError:
    ...
# import teste
print(modulos.soma(4, 5))
print(soma(5, 6))
print('Este modo se chama', __name__) #Caso seja o primeiro módulo a ser executado, ele receberá o nome __main__