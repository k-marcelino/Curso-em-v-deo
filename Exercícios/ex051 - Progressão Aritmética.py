'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

t = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da pa: "))
decimo = t + (10 - 1) * r
for i in range(t, decimo + r, r):
    print(i)