# limpa tela
import os
os.system('cls || clear') or None

# função
def soma(a, b, c):
    """Soma valores entre b e c que sejão divisíveis por a"""
    # variável
    s = 0

    # controle
    if a > 1:
        # iteração
        for i in range(b, c + 1):
            # controle
            if i % a == 0:
                s += i
    else:
        print('O valor de \'a\' deve ser maior do que 1.')
    
    return s

# input
a = int(input('Entre com o valor de a: '))
b = int(input('Entre com o valor de b: '))
c = int(input('Entre com o valor de c: '))

# chamar função
resultado = soma(a, b, c)

# output
print(f'O resultado da soma é {resultado}.')