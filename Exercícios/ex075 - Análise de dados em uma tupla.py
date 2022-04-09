'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

# Coletando os valores
analise = []
for valor in range(4):
    n = int(input("Digite um valor: "))
    analise.append(n)

# Daria pra fazer sem usar loop e converter
'''n = (int(input("Digite um valor: ")),
     int(input("Digite um valor: ")),
     int(input("Digite um valor: ")),
     int(input("Digite um valor: ")))'''

# Convertendo em tupla
analise = tuple(analise)

# Prints
print(f'Você digitou {analise.count(9)} vezes o número 9')
print(f'A posição do primeiro digito 3 é: {analise.index(3)}' if 3 in analise else "3 não encontrado")
print(f'Números pares: ', end='')
for i in analise:
    if i % 2 == 0:
        print(f'{i} ', end='')
