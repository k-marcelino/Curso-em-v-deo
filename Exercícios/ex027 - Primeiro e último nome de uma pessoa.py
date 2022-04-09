'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente. '''

nome = str(input('Digite seu nome completo: ')).strip()

split = nome.split()
size = len(split)

print(f'Seu primeiro nome é: {split[0]}')
print(f'Seu último nome é: {split[size - 1]}')
