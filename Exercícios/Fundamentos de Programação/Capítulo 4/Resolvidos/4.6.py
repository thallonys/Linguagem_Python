# limpa tela
import os
os.system('cls || clear') or None

# input
numero = int(input('Informe um número: '))

# output
if numero % 2 == 0:
    print(f'{numero} é par.')
else:
    print(f'{numero} é impar.')