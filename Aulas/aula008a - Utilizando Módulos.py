'''Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import
e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos
adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.'''


import math
# se apertar ctrl + space depois do from math import, irá mostrar todas as funcionalidades da biblioteca
# nesse caso não precisa colocar o "math.sqrt" no programa, só sqrt() já basta
# from math import sqrt, floor, etc
n = int(input("Digite um número: "))
sqr = math.sqrt(n)

print(f"A raíz de {n} é igual a {sqr}")
