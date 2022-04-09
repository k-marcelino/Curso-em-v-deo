'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

size = int(input("Digite a quantidade de alunos a ser sorteados: "))
alunos = []

for i in range(size):
    aluno = str(input(f"Digite o nome do aluno: "))
    alunos.append(aluno)

nome_aleatorio = random.choice(alunos)
print(f'O aluno(a) escolhido(a) foi: {nome_aleatorio}')
