# imports
import os

# limpa tela
os.system('cls || clear') or None

# input
print('Primeira data:')

dia1 = int(input('Entre com o dia da primeia data: '))
mes1 = int(input('Entre com o mês da primeira data: '))
ano1 = int(input('Entre com o ano da primeira data: '))

print('Segunda data:')

dia2 = int(input('Entre com o dia da segunda data: '))
mes2 = int(input('Entre com o mês da segunda data: '))
ano2 = int(input('Entre com o ano da segunda data: '))

#output
if ano1 > ano2:
    print(f'{dia2}/{mes2}/{ano2} - Essa data é a maior.')
elif ano1 < ano2:
    print(f'{dia1}/{mes1}/{ano1} - Essa data é a maior.')
elif ano1 == ano2 and mes1 > mes2:
    print(f'{dia2}/{mes2}/{ano2} - Essa data é a maior.')
elif ano1 == ano2 and mes1 < mes2:
    print(f'{dia1}/{mes1}/{ano1} - Essa data é a maior.')
elif ano1 == ano2 and mes1 == mes2 and dia1 > dia2:
    print(f'{dia2}/{mes2}/{ano2} - Essa data é a maior.')
elif ano1 == ano2 and mes1 == mes2 and dia1 < dia2:
    print(f'{dia1}/{mes1}/{ano1} - Essa data é a maior.')
elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
    print('As datas são iguais.')