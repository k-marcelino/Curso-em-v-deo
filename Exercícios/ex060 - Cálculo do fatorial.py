'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input("Digite um número para saber seu fatorial: "))
fatorial = 1

while n >= 2:
    fatorial *= n
    n -=1

print(f"O fatorial é: {fatorial}")