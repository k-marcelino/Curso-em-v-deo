'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n = int(input("Digite um número: "))
n2 = n * 2
n3 = n * 3
nroot = n**(1/2)

print("O dobro de {} é {}\nO tripo de {} é {}\ne sua raíz quadrada é: {:.3f}".format(n, n2, n, n3, nroot))
