# limpa tela
import os
os.system('cls || clear') or None

# input
valorDepostio = float(input('Informe o valor do depósito: '))
valorTaxaJuros = float(input('Informe o valor da taxa de juros: '))

# cálculo
valorTaxaJuros = valorTaxaJuros / 100
valorRendimento = valorTaxaJuros * valorDepostio
valorTotal = valorRendimento + valorDepostio

# output
print('O valor do rendimento é de R$', valorRendimento, end='.\n')
print('O valor total é de R$', valorTotal, end='.')