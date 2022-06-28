# limpa tela
import os
os.system('cls || clear') or None

# input
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
numero3 = float(input('E outro: '))

# output
if numero1 < numero2 and numero2 < numero3:
    print(numero1, numero2, numero3, sep=', ', end='.')
if numero1 < numero2 and numero1 < numero3 and numero2 > numero3:
    print(numero1, numero3, numero2, sep=', ', end='.')
if numero2 < numero1 and numero1 < numero3:
    print(numero2, numero1, numero3, sep=', ', end='.')
if numero2 < numero1 and numero2 < numero3 and numero1 > numero3:
    print(numero2, numero3, numero1, sep=', ', end='.')
if numero3 < numero1 and numero1 < numero2:
    print(numero3, numero1, numero2, sep=', ', end='.')
if numero3 < numero1 and numero3 < numero2 and numero1 > numero2:
    print(numero3, numero2, numero1, sep=', ', end='.')