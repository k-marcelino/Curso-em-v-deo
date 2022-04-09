'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.'''

n = int(input("Quantas pessoas vamos analisar?: "))

soma_idade = 0
maior_idade_m = 0
nome_m = ''
totmulher20 = 0
for i in range(1, n+1):
    print(f'{i}ª Pessoa')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]:')).strip().lower()
    if sex == 'm' and age > maior_idade_m:
        maior_idade_m = age
        nome_m = name
    if sex == 'f' and age < 20:
        totmulher20 += 1

    soma_idade +=age

print(f'A média de idade do gruo é de: {soma_idade/n} anos')
print(f'O homem mais velho do grupo é o {nome_m}, com {maior_idade_m} anos')
print(f'No grupo existem {totmulher20} mulheres com menos de 20 anos')