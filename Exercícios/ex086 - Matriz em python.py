'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

lista = []
swap = []

for i in range(3):
    for j in range(3):
        swap.append(int(input(f"Digite um valor para [{i}, {j}]: ")))

    lista.append(swap[:])
    swap.clear()

for i in lista:
    print(i)
