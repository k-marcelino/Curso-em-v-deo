'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

n1 = input(f"Digite o nome do 1º aluno: ")
n2 = input(f"Digite o nome do 2º aluno: ")
n3 = input(f"Digite o nome do 3º aluno: ")
n4 = input(f"Digite o nome do 4º aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(lista)