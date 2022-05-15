# A mesma variável pode assumir diferentes tipos
"""
Python é conhecido por não term ponto e vírgula.
Porém, isso é uma meia verdade, pois, no lugar
do ponto e vírgua, é usado o ENTER. Todavia,
se for necessário declarar mais "comandos" em
uma mesma linha, ai sim, usa-se ponto e vírgula.
"""
canal = "CFB Cursos"
curso = "Curso de Python"; nome = "euMesmoEIrene"
print(canal)
print(curso)
print(nome)
# Contatenação
print(canal + " - " + curso)

# Sobre escopo:
"""
O delimitador de escopo no python é a identação.
Assim, o mesmo tamanho da identação deve ser igual
para as todas as declarações ficarem no escopo.
"""
if 10 > 2:
    print("Maior")
    print("aula 2")
print("FIM")
