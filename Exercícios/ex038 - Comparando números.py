'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

print("Digite dois números abaixo para comparar e saber qual deles é o maior")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print(f"O primeiro número ({n1}) é o maior")
elif n1 < n2:
    print(f"O segundo número ({n2}) é o maior")
else:
    print("Os números são iguais")
