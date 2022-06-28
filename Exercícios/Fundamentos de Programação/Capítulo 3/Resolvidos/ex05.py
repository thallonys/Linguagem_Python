# limpa tela
import os
os.system('cls || clear') or None

# input
salario = float(input('Informe o valor do salário: '))
aumento = float(input('Informe o valor da porcentagem do aumento: '))

# cálculo
aumento = aumento / 100
novoSalario = aumento * salario + salario

# output
print('O valor do novo salário é de R$', novoSalario, end='.')