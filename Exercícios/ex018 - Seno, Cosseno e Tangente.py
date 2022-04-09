'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo. '''

import math

n = int(input("Digite um ângulo qualquer: "))

seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangent = math.tan(math.radians(n))

print(f"Seno = {seno:.2f}\nCosseno = {cosseno:.2f}\nTangente = {tangent:.2f}")