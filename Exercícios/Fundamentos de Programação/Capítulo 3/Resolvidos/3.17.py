# limpa tela
import os
os.system('cls || clear') or None

# input
valorDeposito = float(input('Informe o valor depositado: '))
valorCheque1 = float(input('Informe o valor do cheque 1: '))
valorCheque2 = float(input('Informe o valor do cheque 2: '))

# cálculo
cpmf1 = 0.38 / 100 * valorCheque1
cpmf2 = 0.38 / 100 * valorCheque2
valorRestante = valorDeposito - cpmf1 - cpmf2 - valorCheque1 - valorCheque2

# output
print(f'O valor restante na conta é de R$ {valorRestante}.')