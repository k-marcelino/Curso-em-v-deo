'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

withdrawal = int(input("Qual o valor a ser sacado? [Apenas números inteiros]: $"))
rest = withdrawal
fifty = twenty = ten = one = 0

while rest > 0:
    fifty = withdrawal // 50
    rest = withdrawal % 50

    twenty = rest // 20
    rest %= 20

    ten = rest // 10
    rest %= 10

    one = rest // 1
    rest %= 1

print('Total de notas:')
print(f'Notas de 50: {fifty} \nNotas de 20: {twenty} \nNotas de 10: {ten} \nNotas de 1 : {one}')
