'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))
    if i == 0:
        greater = lista[i]
        smaller = lista[i]
    if lista[i] > greater:
        greater = lista[i]
    elif lista[i] < smaller:
        smaller = lista[i]

print(f'Valores Digitados: {lista}')
print(f'O maior valor digitado foi: {greater} nas posições: ', end='')
for pos, i in enumerate(lista):
    if i == greater:
        print(f'{pos}..', end='')
print(f'\nO menor valor digitado foi: {smaller} nas posições: ', end='')
for pos, i in enumerate(lista):
    if i == smaller:
        print(f'{pos}..', end='')
