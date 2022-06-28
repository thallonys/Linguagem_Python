# limpa tela
import os
os.system('cls || clear') or None

#input
print('Informe três números em ordem crescente. Depois, informe um quarto qualquer.')
numero1 = float(input('O primeiro: '))
numero2 = float(input('O segundo: '))
numero3 = float(input('O terceiro: '))
numero4 = float(input('O quarto: '))

# output
if numero1 < numero2 and numero2 < numero3:
    if numero4 > numero3:
        print(numero1, numero2, numero3, numero4, sep=', ', end='.')
    elif numero4 > numero2:
        print(numero1, numero2, numero4, numero3, sep=', ', end='.')
    elif numero4 > numero1:
        print(numero1, numero4, numero2, numero3, sep=', ', end='.')
    else:
        print(numero4, numero1, numero2, numero3, sep=', ', end='.')
else:
    print('Sequência errada. Lembre-se, os três primeiros números devem ser digitados de forma crescente... crescente... crescente...')
