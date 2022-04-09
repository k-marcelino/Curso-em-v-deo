'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

count = 0
for i in range(1, 501): # mesmo esquema do anterior, daria pra colocar o step = 2 e ficar mais eficiente
    if i % 3 == 0 and i % 2 == 1:
        count +=1

print(f'A soma de todos os números entre 1 e 500 que são ímpares e múltiplos de 3 é: {count}')