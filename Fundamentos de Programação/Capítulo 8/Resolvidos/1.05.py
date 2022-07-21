# limpa tela
import os
os.system('cls || clear') or None

# função
def diferenciar(valorAntigo, valorAtual):
    """Calcula o percentual de aumento"""
    # cálculo
    aumento_percentual = (valorAtual - valorAntigo) / valorAntigo * 100
    
    # retornar
    return aumento_percentual

# input
valorAntigo = float(input('Entre com o valor antigo da mercadoria: '))
valorAtual = float(input('Entre com o valor atual da mercadoria: '))

# chamar função
resultado_aumento = diferenciar(valorAntigo, valorAtual)

# output
print(f'O percentual de aumento é de %{resultado_aumento}.')