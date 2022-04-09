#Faça um programa que leia um número inteiro qualquer e mostra na tela a sua tabuada

n = int(input("Digite um número inteiro para saber sua tabuada: "))
i = 1
while i <= 10:
    print("{} x {:2} = {}".format(n, i, n * i))
    print("-" * 10)
    i = i + 1

