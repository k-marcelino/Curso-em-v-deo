'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math

cat_oposto = float(input("Digite a medida do cateto oposto: "))
cat_adj = float(input("Digite a medida do cateto adjacente: "))

hip = math.hypot(cat_oposto, cat_adj)
print(f"A hipotenusa é: {hip:.2f}")
