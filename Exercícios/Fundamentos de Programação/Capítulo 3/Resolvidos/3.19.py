# limpa tela
import os
os.system('cls || clear') or None

# input
alturaDegrau = float(input('Altura do degrau em metros: '))
alturaAlmejada = float(input('Algura Almejada: '))

# cálculo
quantidadeDegraus = alturaAlmejada / alturaDegrau

# output
print(f'A quantidade de degraus necessária é {quantidadeDegraus}.')