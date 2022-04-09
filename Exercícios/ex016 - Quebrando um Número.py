'''Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na
tela a sua porção Inteira.'''


from math import trunc

n = float(input("Digite um número qualquer com decimal: "))
print(f"O número digitado foi {n} e o número quebrado é {trunc(n)}")

# ou apenas:

m = int(n)
print(m)
