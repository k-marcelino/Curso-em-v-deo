'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

eighteen = male = young_female = 0

while True:
    age = int(input("Digite a idade: "))
    gender = ' '

    while gender not in 'mf':
        gender = str(input("Digite o sexo [M/F]: ")).lower().strip()[0]

    if age > 18:
        eighteen += 1
    if gender == 'm':
        male += 1
    if gender == 'f' and age < 20:
        young_female += 1

    answer = ' '
    while answer not in 'sn':
        answer = str(input("Você quer continuar o cadastramento? [S/N]:")).lower().strip()[0]
    if answer == 'n':
        break

print(f"\nPessoas maiores de 18 anos: {eighteen}")
print(f'Homens no grupo: {male}')
print(f'Mulheres abaixo de 20 anos: {young_female}')