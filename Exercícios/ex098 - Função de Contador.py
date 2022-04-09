'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''


def contador():
    from time import sleep
    # Primeiro tipo automático
    print(f'Contagem do tipo 1:')
    for i in range(1, 11, 1):
        print(f' {i} ', end='')
        sleep(0.1)
    print()

    # Segundo tipo automático
    print(f'Contagem do tipo 2:')
    for i in range(10, -1, -2):
        print(f' {i} ', end='')
        sleep(0.1)

    # Personalizado
    print("\nContagem Personalizada: ")
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    # Parte para ajustar, pois o fim é sempre exclusivo no range, mas aqui ele tem que mostrar
    if fim > inicio:
        fim += 1
    else:
        fim -= 1
    # Ajuste para passo em diversas situações, caso a contagem seja regressiva por exemplo
    passo = int(input('Passo: '))
    if inicio > fim and passo > 0:
        passo *= -1
    elif inicio > fim and passo == 0:
        passo = -1
    elif inicio < fim and passo == 0:
        passo = 1
    # Output final
    print(f'Contagem do tipo 3 - Personalizada')
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
        sleep(0.1)


contador()
