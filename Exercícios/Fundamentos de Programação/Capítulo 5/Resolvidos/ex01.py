# limpa tela
import os
os.system('cls || clear') or None

# variáveis
anoInicial = 2005
salarioInicial = 1000
aumento = 1.5
anoAtual = 0
salario = 0
count = 1

# output
while(anoAtual != 2022):
    anoAtual = anoInicial + count
    count += 1
    salario = (aumento / 100) * salarioInicial + salarioInicial
    aumento *= 2
    print(f'O valor do salário em {anoAtual} é de {salario}.') 



