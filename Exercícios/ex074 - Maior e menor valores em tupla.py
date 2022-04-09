'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.'''
from random import randint

# Gerando números aleatoriamente
numbers = []
for i in range(0, 5):
    numbers.append(randint(0, 100))

# Também daria pra fazer:
#n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

# Convertendo para tupla
numbers = tuple(numbers)
print(type(numbers))
print(numbers)

# Prints
print(f'O maior número é {max(numbers)}')
print(f'O menor número é {min(numbers)}')
