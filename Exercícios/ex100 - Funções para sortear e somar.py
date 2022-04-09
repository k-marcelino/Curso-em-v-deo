'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da
lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
numeros = []


def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 100))
    print(f"Números sorteados: {numeros}")


def somaPar():
    sum = 0
    for i in numeros:
        if i % 2 == 0:
            sum += i
    print(f"A soma dos números pares da lista é: {sum}")


sorteia()
somaPar()
