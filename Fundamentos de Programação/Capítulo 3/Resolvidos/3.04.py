# limpa tela
import os
os.system('cls || clear') or None

# input
salario = float(input('Informe o valor do salário: '))

# cálculo
aumento = 25 / 100
novoSalario = aumento * salario + salario

# output
print('O valor do novo salário é', novoSalario, end='.')