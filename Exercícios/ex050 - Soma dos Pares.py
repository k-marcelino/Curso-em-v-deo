'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
count = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}º número inteiro: '))
    if n % 2 == 0:
        soma += n
        count += 1

print(f'A soma dos {count} números pares fornecidos é: {soma}')