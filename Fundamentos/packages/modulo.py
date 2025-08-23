# Caso o import seja feito dessa forma 'from packages.modulo import *', apenas o que está dentro do __all__ irá aparecer no import
__all__ = [
    'soma_modulo',
    'variavel',
]

from packages.modulo_b import ola

variavel = 'Breno'
def soma_modulo(x, y):
    return x + y

print(ola())