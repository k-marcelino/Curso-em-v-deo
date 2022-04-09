'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
r = 0

while r != 5:
    sleep(2)
    print('MENU ' + "#" * 10 +
    '\n[1]SOMAR'
    '\n[2]MULTIPLICAR'
    '\n[3]MAIOR'
    '\n[4]NOVOS NÚMEROS'
    '\n[5]SAIR DO PROGRAMA')
    r = int(input("\nDigite o valor correspondente ao comando: "))

    if r == 1:
        print(f"A soma de {n1} + {n2} = {n1 + n2}")
    elif r == 2:
        print(f"O produto de {n1} * {n2} = {n1 * n2}")
    elif r == 3:
        print(f"O maior número entre {n1} e {n2} = {max(n1, n2)}")
    elif r == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif r == 5:
        print("Fim de Programa")