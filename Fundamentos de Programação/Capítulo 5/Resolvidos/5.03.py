# limpa tela
import os
os.system('cls || clear') or None

# variáveis
fatorial = 1
count = 0

# input
N = int(input('Informe um inteiro positivo: '))

# cálulo
if N < 0:
    print('Escolha errada!')
else: 
    for num in range(1, N + 1):
        count += 1
        fatorial *= num
    print(f'O valor {count} e seu fatorial {fatorial}.') 


