'''Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.'''

n = int(input("Digite um número para saber se é par ou impar: "))

print(f"O número {n} é par!" if n % 2 == 0 else f"O número {n} é impar")
