'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

size = int(input("Digite a quantidade de alunos a ser sorteados: "))
i = 0
alunos = []

while i < size:
    aluno = str(input(f"Digite o nome do aluno: "))
    alunos.append(aluno)
    i += 1

nome_aleatorio = random.choice(alunos)
print(f'O aluno(a) escolhido(a) foi: {nome_aleatorio}')

#não funcionou, tentar novamente depois de assistir mais vídeos
#dia 03/04/2022 - voltei aqui por acaso e resolvi o problema :)