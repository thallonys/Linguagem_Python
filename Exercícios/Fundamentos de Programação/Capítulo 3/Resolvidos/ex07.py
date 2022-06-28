# limpa tela
import os
os.system('cls || clear') or None

# input
salarioBase = float(input('Informe o valor do salário base: '))

# cálculo
gratificacao = 50
imposto = 10 / 100
salarioReceber = gratificacao + salarioBase - imposto * salarioBase

# output
print('O valor do salário a receber é de R$', salarioReceber, end='.')