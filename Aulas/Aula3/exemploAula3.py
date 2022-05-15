# Escopo de variáveis
"""
A variável declara fora de qualquer função é acessível a qualquer
parte do programa. Porém, se declara dentre de uma função, ela tem
seu acesso limitado. Todavia, se essa variável for configurada para
ser global, ai sim, poderá ser acesso por qualquer parte do programa
independentemente de estar ou não for de alguma função.
"""


def cn():
    global canal
    canal = "alguma coisa"


cn()

print(canal)
