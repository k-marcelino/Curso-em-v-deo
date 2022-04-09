'''Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão
no intervalo entre 1 e 50. '''
count = 0

# ou poderia colocar o step = 2 e não verificar se é par, apenas somar
for i in range(1,51):
    if i % 2 == 0:
        count += i
        print(i, end=' ')

print(f'\nA soma dos números entre 1 e 50 que são pares é de: {count}')