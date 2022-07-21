# limpa tela
import os
os.system('cls || clear') or None

# variáveis
E = 1

# input
N = int(input('Informe um inteiro positivo: '))

# cálculo
for fatorial in range(1, N + 1):
    fatorial *= fatorial
    E = E + (1 / fatorial)
    
print(E)