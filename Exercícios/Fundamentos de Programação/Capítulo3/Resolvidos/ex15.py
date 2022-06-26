# limpa tela
import os
os.system('cls || clear') or None

# input
precoFabrica = float(input('Informe o preço de fábrica do carro: '))
percentualLucro = float(input('Informe o percentual de lucro do distribuidor: '))
percentualImposto = float(input('Informe o percentual de imposto: '))

# cálculo
valorDistribuidor = percentualLucro / 100 * precoFabrica
valorImpsoto = percentualImposto / 100 * precoFabrica
precoFinal = precoFabrica + valorDistribuidor + valorImpsoto

# output
print('O valor do distrituido é de R$', valorDistribuidor)
print('O valor do imposto é de R$', valorImpsoto)
print('O preço final do carro é de R$', precoFinal)