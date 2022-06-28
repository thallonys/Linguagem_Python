# limpa tela
import os
os.system('cls || clear') or None

# input
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))

# output
if numero1 > numero2:
    print(numero1, 'é maior do que', numero2, end='.')
elif numero1 < numero2:
    print(numero2, 'é maior do que', numero1, end='.')
else:
    print('Os números são iguais.')