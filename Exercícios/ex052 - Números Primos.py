'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo. '''


n = int(input("Digite um número para verificar se é primo: "))
count = 0
for i in range(2, n + 1):
    if n % i == 0:
        count += 1

if count == 1 or n == 1:
    print(f'O número {n} É primo')
else:
    print(f'O número {n} NÃO é primo')