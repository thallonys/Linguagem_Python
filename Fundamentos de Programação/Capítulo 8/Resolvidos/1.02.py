# limpa tela
import os
os.system('cls || clear') or None

# função
def soma_entre_valores(x, y):
    """Soma valores entre x e y"""
    # variável
    s = 0

    # iteração
    for i in range(x, y + 1):
        s += i 
    # output
    print(f'A soma é {s}.')

# input
x = int(input('Entre com um valor: '))
y = int(input('Entre com outro valor: '))

# chamar função
soma_entre_valores(x, y)

