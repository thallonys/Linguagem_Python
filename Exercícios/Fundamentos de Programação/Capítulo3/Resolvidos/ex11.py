# limpa tela
import os
os.system('cls || clear') or None

# input
numero = int(input('Insira um número maior do que zero: '))

# cálculo
quadrado = numero * numero
cubo = quadrado * numero
raizQuadrada = numero ** (1/2)
raizCubica = numero ** (1/3)

# output
print('O valor do número ao quadrado é', quadrado)
print('O valor do número ao cubo é', cubo)
print('O valor da raiz quadrada do número é', raizQuadrada)
print('O valor da raiz cubida do número é', raizCubica)