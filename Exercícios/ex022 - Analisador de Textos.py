'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome totalmente em letras maiúsculas é = {nome.upper()}')
print(f'Seu nome totalmente em letras maiúsculas é = {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
#desse jeito é encontrado onde vem o primeiro "espaço" e é contado até ele
print(f'Seu primeiro nome tem {nome.find(" ")} letras')

#ou splitar o nome:
#first = nome.split()
#print(len(first[0]))
