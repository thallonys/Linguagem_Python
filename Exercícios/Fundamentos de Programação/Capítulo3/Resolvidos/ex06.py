# limpa tela
import os
os.system('cls || clear') or None

# input
salarioBase = float(input('Informe o valor do salário: '))

# cálculo
gratificacao = 5 /100
imposto = 7 / 100
salarioReceber = gratificacao * salarioBase + salarioBase - imposto * salarioBase

# output
print('O salario a receber é de R$', salarioReceber)
