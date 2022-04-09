'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

swap = []
pessoas = []
heaviest = lightest = 0

while True:
    swap.append(str(input('Digite o Nome da pessoa: ')))
    swap.append(float(input('Digite o peso da pessoa: ')))

    if len(pessoas) == 0:
        heaviest = lightest = swap[1]
    else:
        if swap[1] > heaviest:
            heaviest = swap[1]
        elif swap[1] < lightest:
            lightest = swap[1]

    pessoas.append(swap[:])
    swap.clear()

    exit = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
    if exit == 'n':
        break

print(f"Você cadastrou {len(pessoas)} pessoas")
print(f'O maior peso foi {heaviest}Kg, de ', end='')
for i in pessoas:
    if i[1] == heaviest:
        print(f'[{i[0]}]..', end='')
print(f'\nO menor peso foi {lightest}Kg, de ', end='')
for i in pessoas:
    if i[1] == lightest:
        print(f'[{i[0]}]..', end='')
