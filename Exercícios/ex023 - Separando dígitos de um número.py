'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados.'''

n = input('Digite um número de 0 a 9999: ')

i = 0
size = len(n)

while i < size:
    print(n[i])
    i += 1
