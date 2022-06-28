# limpa tela
import os
os.system('cls || clear') or None

# variáveis e input
nota1 = float(input('Insira a primeira nota: '))
peso1 = float(input('Insira seu respectivo peso: '))

nota2 = float(input('Insira a segunda nota: '))
peso2 = float(input('Insira seu respectivo peso: '))

nota3 = float(input('Insira a terceira nota: '))
peso3 = float(input('Insira seu respectivo peso: '))

# cálculo
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# output
print('A média ponderada é', media, end='.')
