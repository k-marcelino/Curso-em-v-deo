'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

cadastro = []
mulheres = []
pessoa = {}
exit = ' '
soma = media = 0

# Obtenção de dados do cadastro
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().lower()
        if pessoa['Sexo'] in 'mf':
            if pessoa['Sexo'] == 'f':
                mulheres.append(pessoa['Nome'])
            break
        print("Erro! Digite apenas 'm' ou 'f'")

    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    cadastro.append(pessoa.copy())

    while True:
        exit = str(input("Deseja Continuar? [S/N]: ")).strip().lower()[0]
        if exit in 'sn':
            break
        print("Erro! Digite apenas 's' ou 'n'")
    if exit == 'n':
        break

media = soma/len(cadastro)
# A
print(f'Pessoas cadastradas: {len(cadastro)}')
# B
print(f'Média de idades do grupo: {media:.2f}')
# C
print(f'Lista apenas com mulheres: {mulheres}')
# D
print(f'Lista de pessoas acima da média: ')
for i in cadastro:
    if i['Idade'] >= media:
        print(i)
