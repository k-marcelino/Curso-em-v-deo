'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

# extrai o ano de acordo com o sistema do computador
ano = date.today().year
maioridade = 18
menores = 0
maiores = 0

for i in range(0, 7):
    nasc = int(input("Digite o seu ano de nascimento no formato (aaaa): "))
    if ano - nasc < maioridade:
        menores += 1
    else:
        maiores += 1

print(f'{menores} pessoas ainda não atigiram a maioridade, e\n'
      f'{maiores} pessoas já atingiram a maioridade')