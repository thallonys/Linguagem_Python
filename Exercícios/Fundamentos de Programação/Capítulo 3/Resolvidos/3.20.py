# imports
import math
import os

# limpa tela
os.system('cls || clear') or None

# input
anguloEscada = float(input('Informe o ângulo da escada: '))
alturaParede = float(input('Informe a altura da parede: '))

# cálculo
radiano = math.radians(anguloEscada)
# radiano = anguloEscada * 3.14 / 180
escada = alturaParede / math.sin(radiano)

# output
print(f'A altura da escada é {escada}.')