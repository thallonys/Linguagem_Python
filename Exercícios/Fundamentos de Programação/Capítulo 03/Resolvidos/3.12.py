# limpa tela
import os
os.system('cls || clear') or None

# input
numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))

# cálculo
resultado = pow(numero1, numero2)

# output
print('O primeiro número elevado ao segundo número é', resultado, end='.')