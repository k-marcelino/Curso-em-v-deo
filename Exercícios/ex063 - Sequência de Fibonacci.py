'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 '''

n = int(input("Quantos termos da função fibonacci gostaria de ver?: "))
i = 1
anterior = 0
next = 1
swap = 0

print(f"{anterior} >", end='')
while i < n:
    print(f" {next} >", end='')
    swap = next
    next = next + anterior
    anterior = swap
    i +=1

print(' FIM')
