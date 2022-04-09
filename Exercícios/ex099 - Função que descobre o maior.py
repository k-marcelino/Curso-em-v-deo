'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*num):
    if len(num) > 0:
        m = max(num)
        print(f'Valores passados: {num} totalizando {len(num)}, elementos')
        print(f"O maior número passado foi {m}")
    else:
        print("Você não informou nenhum valor")
    print('#' * 40)


maior(1, 100, 1000, 9999)
maior()
