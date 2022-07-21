# limpa tela
import os
os.system('cls || clear') or None

# função
def verifica_numero(x):
    """Verifica se o número é negativo ou positivo"""
    #iteração
    if x >= 0:
        # output
        print(1)
    else:
        # output
        print(0)

# input
x = int(input('Entre com um inteiro: '))

# chamar função
verifica_numero(x)