'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

lista = []
swap = []
par = third_c = second_l = 0

for i in range(3):
    for j in range(3):
        swap.append(int(input(f"Digite um valor para [{i}, {j}]: ")))

        if swap[j] % 2 == 0:
            par += swap[j]
        if j == 2:
            third_c += swap[j]
        if i == 1:
            second_l = max(second_l, swap[j])

    lista.append(swap[:])
    swap.clear()

for i in lista:
    print(i)

print(f'\nSoma dos valores pares: {par}')
print(f'Soma dos valores da terceira coluna: {third_c}')
print(f'Maior valor da segunda linha: {second_l}')
