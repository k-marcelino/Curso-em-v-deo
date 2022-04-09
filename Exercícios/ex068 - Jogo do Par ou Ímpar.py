'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo. '''

from random import randint

soma = count = 0
while True:
    pc = randint(0, 11)
    n = ' '

    while n not in 'pi':
        n = str(input('Você escolhe Par ou Ímpar? [P/I]: ')).lower().strip()[0]

    player = int(input('Escolha um número: '))
    soma = pc + player

    if soma % 2 == 0:
        print(f'O computador jogou {pc} + sua jogada {player} deu {soma}, gerando um número Par')
        if n == 'p':
            print('Parabéns você venceu!')
        else:
            print(f'Game Over! Você venceu {count} vezes seguidas ')
            break
    else:
        print(f'O computador jogou {pc} + sua jogada {player} deu {soma}, gerando um número Ímpar')
        if n == 'i':
            print('Parabéns você venceu!')
        else:
            print(f'Game Over! Você venceu {count} vezes seguidas ')
            break
    count += 1
