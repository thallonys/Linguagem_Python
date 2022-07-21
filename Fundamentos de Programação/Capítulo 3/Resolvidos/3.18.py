# limpa tela
import os
os.system('cls || clear') or None

# input
pesoSaco = float(input('Informe o peso do saco em quilos: '))
porcaoGato = float(input('Quantidade de porção em gramas fornecida aos gatos: '))
dias = int(input('Quantidade de dias: '))

# cálculo
pesoSaco *= 1000
restoRacao = pesoSaco - dias * porcaoGato
restoRacao /= 1000

# output
print(f'Depois de 5 dias restará {restoRacao} de ração.')