# imports
import os
import math

# limpa tela
os.system('cls || clear') or None

#input
opcao = int(input('Menu de ações: \n'
        '1. Somar dois números \n'
        '2. Raiz quadrada de um número \n'
        'Digite a opção desejada: '))

if opcao == 1:
    #input 
    numero1 = float(input('Entre com o primeiro número: '))
    numero2 = float(input('Entre com o segundo número: '))

    # Cálculo
    resultado = numero1 + numero2

    #output
    print(f'O resultado da soma é {resultado}.')

if opcao == 2:
    # input
    numero = int(input('Entre com um número: '))

    # cálculo
    resultado = math.sqrt(numero)

    # output
    print(f'A raiz quadrada é {resultado}')