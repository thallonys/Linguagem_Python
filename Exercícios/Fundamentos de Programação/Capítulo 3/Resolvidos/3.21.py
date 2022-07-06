# imports
import os
import math

# limpa tela
os.system('cls || clear') or None

#input
tamanhoEscada = float(input('Informe o tamanho da escada: '))
alturaQuadro = float(input('Informe a altura em que o quadro será fixado: '))

#cálculo
distancia = math.sqrt(tamanhoEscada ** 2 - alturaQuadro ** 2)

#output
print(f'A distância em que a escava de ficar é {distancia}.')
