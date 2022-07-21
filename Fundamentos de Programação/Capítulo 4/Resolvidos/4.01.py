# limpa tela
import os
os.system('cls || clear') or None

# variáveis
peso1 = 2
peso2 = 3
peso3 = 5

# input
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

# cálculo
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# output
if media >= 8 and media <= 10:
    print('A média é', media, 'e o conceito é A', end='.')
elif media >= 7 and media < 8:
    print('A média é', media, 'e o conceito é B', end='.')
elif media >= 6 and media < 7:
    print('A média é', media, 'e o conceito é C', end='.')
elif media >= 5 and media < 6:
    print('A média é', media, 'e o conceito é D', end='.')
elif media >= 0 and media < 5:
    print('A média é', media, 'e o conceito é E', end='.')