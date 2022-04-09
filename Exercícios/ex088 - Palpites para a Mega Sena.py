'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint

n = int(input("Quantos jogos quer que eu sorteie?: "))
lista = []

for i in range(n):
    while len(lista) < 6:
        jogo = randint(1, 60)
        if jogo not in lista:
            lista.append(jogo)

    lista.sort()
    print(f'Jogo {i + 1}: {lista}')
    lista.clear()
