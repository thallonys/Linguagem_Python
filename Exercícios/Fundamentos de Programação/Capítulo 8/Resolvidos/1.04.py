# limpa tela
import os
os.system('cls || clear') or None

# função
def converter(segundos):
    """Converte segundos em minutos e horas"""
    # cálculo
    horas = segundos / 3600 
    minutos = segundos / 60

    # output
    print(f'Segundos em horas = {horas}')
    print(f'Segundos em minutos = {minutos}')

# input
x = int(input('Entre com uma quantidade de segundos: '))

# chamar função
converter(x)