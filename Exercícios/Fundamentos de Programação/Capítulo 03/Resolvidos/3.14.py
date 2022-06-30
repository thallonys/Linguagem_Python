# limpa tela
import os
os.system('cls || clear') or None

# input
anoNascimento = int(input('Informe o ano de nascimento: '))
anoAtual = int(input('Informe o ano atual: '))

# cálculo
idade = anoAtual - anoNascimento
anoFuturo = 2050
idadeFutura = anoFuturo - anoNascimento

# output
print('Sua idade é', idade, end='.\n')
print('Sua idade em', anoFuturo, 'é', idadeFutura, end='.')