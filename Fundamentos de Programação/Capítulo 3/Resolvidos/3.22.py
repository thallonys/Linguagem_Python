# imports
import os
import math

# limpa tela
os.system('cls || clear') or None

# input
salarioMinimo = float(input('Valor do salário mínimo: '))
quantidadeQuilowatts = float(input('Quantidade de quilowatts: '))

# cálculo
valorQuilowatts = quantidadeQuilowatts / 5
valorPagoResidencia = valorQuilowatts * quantidadeQuilowatts
valorPagoComDesconto = valorPagoResidencia - (15 / 100 * valorPagoResidencia)

print(f'O valor do quilowatts é de R$ {valorQuilowatts}.')
print(f'O valor a ser pago pela residência é R$ {valorPagoResidencia}')
print(f'O valor a ser pago com desconto de 15% é R$ {valorPagoComDesconto}')