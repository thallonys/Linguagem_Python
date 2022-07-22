# limpa tela
import os
os.system('cls || clear') or None

# variáveis
somaVeiculo = 0
somaAcidentes = 0
contAcidentes = 0

# input
for i in range(1, 6):
    codCidade = int(input(f'Entre com o código da cidade {i}: '))
    numVeiPasseio = int(input('Entre com o número de veículos: '))
    numAcidTransito = int(input('Entre com o número de acidentes de transito: '))

    if i == 1:
        maior = numAcidTransito
        cidadeMaior = codCidade
        menor = numAcidTransito
        cidadeMenor = codCidade
    else:
        if numAcidTransito > maior:
            maior = numAcidTransito
            cidadeMaior = codCidade
        if numAcidTransito < menor:
            menor = numAcidTransito
            cidadeMaior = codCidade

    somaVeiculo += numVeiPasseio

    if numVeiPasseio < 2000:
        somaAcidentes += numAcidTransito
        contAcidentes += 1

print(f'Maior número de acidentes de transito é {maior} na cidade {cidadeMaior}')
print(f'Menor número de acidentes de transito é {menor} na cidade {cidadeMenor}')

media = somaVeiculo / 5

print(f'Media do total de veículos: {media}.')

if contAcidentes == 0:
    print('Não foi digitado uma cidade com menos de 2000 veículos.')
else:
    media = somaAcidentes / contAcidentes
    print(f'Media da quantidade de acidentes: {media}.')
