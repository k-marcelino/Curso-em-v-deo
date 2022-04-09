'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

answer = ['m', 'f']
r = ''
# Dava pra colocar :  while r not in 'MmFf' > seria mais eficiente até
while r not in answer:
    r = str(input('Digite o seu sexo [M/F]: ')).lower().strip()[0]
    print(r)
print('Registrado com Sucesso!')