'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

n1 = input(f"Digite o nome do 1º aluno: ")
n2 = input(f"Digite o nome do 2º aluno: ")
n3 = input(f"Digite o nome do 3º aluno: ")
n4 = input(f"Digite o nome do 4º aluno: ")
lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)
print(f"O aluno(a) escolhido(a) foi: {sorteado}")
