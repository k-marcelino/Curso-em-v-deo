'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = mil = cheap = 0
cheapest = ''

while True:
    name = str(input("Digite o nome do produto: "))
    price = float(input("Digite o preço: "))

    if total == 0 or price < cheap:
        cheap = price
        cheapest = name
    total += price

    if price > 1000:
        mil += 1

    answer = ' '
    while answer not in 'SsNn':
        answer = str(input("Você quer continuar o cadastramento? [S/N]:")).lower().strip()[0]
    if answer == 'n':
        break

print(f'\nTotal gasto na compra $: {total:.2f}')
print(f'{mil} Produtos custam mais do que $1K')
print(f'{cheapest} foi o Produto mais barato custando ${cheap:.2f}')
