'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''


pesos = []

for i in range(5):
    peso = int(input(f"Informe o peso da {i + 1}ª pessoa: "))
    pesos.append(peso)

print(f'O maior peso foi :{max(pesos)} Kg')
print(f'O menor peso foi :{min(pesos)} Kg')
