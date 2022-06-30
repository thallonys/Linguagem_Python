# limpa tela
import os
os.system('cls || clear') or None

# input
print('|                     MENU                               |\n'\
    '| Valor de I |             FORMA A ESCREVER              |\n'\
    '|      1     | A, B e C em ordem crescente               |\n'\
    '|      2     | A, B e C em ordem decrescente             |\n'\
    '|      3     | O maior fica entre os outros dois números |\n')

A = float(input('Informe um número qualquer: '))
B = float(input('Informe outro número: '))
C = float(input('E outro qualquer: '))
I = int(input('Informe o valor de I: '))

# output
if I == 1:
    if A < B and B < C:
        print(A, B, C, sep=', ', end='.')
    elif A < B and C < B and A < C:
        print(A, C, B, sep=', ', end='.')
    elif B < A and A < C:
        print(B, A, C, sep=', ', end='.')
    elif B < A and C < A and B < C:
        print(B, C, A, sep=', ', end='.')
    elif C < A and A < B:
        print(C, A, B, sep=', ', end='.')
    elif C < A and B < A and C < B:
        print(C, B, A, sep=', ', end='.')
elif I == 2:
    if A > B and B > C:
        print(A, B, C, sep=', ', end='.')
    elif A > B and C > B and A > C:
        print(A, C, B, sep=', ', end='.')
    elif B > A and A > C:
        print(B, A, C, sep=', ', end='.')
    elif B > A and C > A and B > C:
        print(B, C, A, sep=', ', end='.')
    elif C > A and A > B:
        print(C, A, B, sep=', ', end='.')
    elif C > A and B > A and C > B:
        print(C, B, A, sep=', ', end='.')
elif I == 3:
    if A < B and B < C:
        print(A, C, B, sep=', ', end='.')
    elif A < B and C < B and A < C:
        print(A, B, C, sep=', ', end='.')
    elif B < A and A < C:
        print(B, C, A, sep=', ', end='.')
    elif B < A and C < A and B < C:
        print(B, A, C, sep=', ', end='.')
    elif C < A and A < B:
        print(C, B, A, sep=', ', end='.')
    elif C < A and B < A and C < B:
        print(C, A, B, sep=', ', end='.')

    elif A > B and B > C:
        print(B, A, C, sep=', ', end='.')
    elif A > B and C > B and A > C:
        print(C, A, B, sep=', ', end='.')
    elif B > A and A > C:
        print(A, B, C, sep=', ', end='.')
    elif B > A and C > A and B > C:
        print(C, B, A, sep=', ', end='.')
    elif C > A and A > B:
        print(A, C, B, sep=', ', end='.')
    elif C > A and B > A and C > B:
        print(B, C, A, sep=', ', end='.')
else:
    print('Opção errada!')
