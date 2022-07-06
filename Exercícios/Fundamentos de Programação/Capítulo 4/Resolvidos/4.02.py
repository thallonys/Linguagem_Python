# limpa tela
import os
os.system('cls || clear') or None

# input
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

# cálculo
media = (nota1 + nota2 + nota3) / 3

# output
if media >= 0 and media < 3:
    print('\nA média é', media, '- Reprovado', end='.')
elif media >= 3 and media < 7:
    print('\nA média é', media, '- Exame:')
    notaExame = 12 - media
    print('Deve tirar', notaExame, 'para ser aprovado', end='.')
elif media >= 7 and media <= 10:
    print('\nA média é', media, '- Aprovado', end='.')