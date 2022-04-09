'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece
a última vez.'''

#colocar em evidência o str para poder usar os comando de objeto nesse caso .lower() e .strip()
frase = str(input('Digite uma frase qualquer: ')).lower() .strip()

print(f"A letra 'a' aparece {frase.count('a')} vezes")
print(f"Apareceu pela primeira vez na posição: {frase.find('a') + 1}")
print(f"E apareceu pela última vez na posição: {frase.rfind('a') + 1}")
