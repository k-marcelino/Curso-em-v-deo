'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os
valores pares e ímpares em ordem crescente.'''

lista = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i + 1}º número: '))

    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(f'Lista completa: {lista}')
print(f'Lista com números pares: {lista[0]}')
print(f'Lista com números ímpares: {lista[1]}')