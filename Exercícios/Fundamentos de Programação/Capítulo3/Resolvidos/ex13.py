# limpa tela
import os
os.system('cls || clear') or None

# input
valorPes = int(input('Informe um valor em pé: '))

# cálculo
polegadas = 12 * valorPes
jardas = 3 * valorPes
milhas = 1760 * jardas

# output
print('O valor em polegadas é', polegadas)
print('O valor em jardas é', jardas)
print('O valor em milhas é', milhas)

