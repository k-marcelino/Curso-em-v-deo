'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['Nome'] = str(input("Nome: "))
aluno['Média'] = float(input("Média: "))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
    print(f'Média de {aluno["Nome"]}: {aluno["Média"]}')

elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
    print(f'Média de {aluno["Nome"]}: {aluno["Média"]}')
else:
    aluno['Situação'] = 'Reprovado'
    print(f'Média de {aluno["Nome"]}: {aluno["Média"]}')

for k, v in aluno.items():
    print(f'{k} é igual a {v}')