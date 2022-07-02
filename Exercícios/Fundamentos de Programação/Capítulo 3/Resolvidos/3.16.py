# limpa tela
import os
os.system('cls || clear') or None

# input
horasTrabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))
valorSalarioMinimo = float(input('Informe o valor do salário mínimo: '))

# cálculo
valorHoraTrabalho = valorSalarioMinimo / 2
salarioBruto = horasTrabalhadas * valorHoraTrabalho
imposto = 3 / 100 * salarioBruto
salarioReceber = salarioBruto - imposto

# output
print(f'O valor do salário a receber é de R$ {salarioReceber}.')
