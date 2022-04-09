'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.'''

import moeda
#from moeda import metade, dobro, aumentar, diminuir

p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {moeda.metade(p):.2f}")
print(f"O dobro de {p} é {moeda.dobro(p):.2f}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10):.2f}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13):.2f}")
