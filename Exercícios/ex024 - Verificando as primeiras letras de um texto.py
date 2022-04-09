'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou
não com o nome “SANTO”.'''
s = input('Digite o nome da sua cidade: ')

s_upper = s.upper()
print('SANTO' in s_upper)
