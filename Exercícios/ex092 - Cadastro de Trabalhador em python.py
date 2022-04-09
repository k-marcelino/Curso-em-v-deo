'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.'''

from datetime import date
trabalhador = {}
ano_atual = date.today().year
temp_aposentadoria = 35

trabalhador['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento [aaaa]: '))
trabalhador['Idade'] = ano_atual - nasc
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): ')) # Carteira de trabalho

if trabalhador['CTPS'] != 0:
    trabalhador['Ano_contr'] = int(input('Ano de contratação [aaaa]: '))
    trabalhador['Salário'] = int(input('Salário: '))
    trabalhador['Aposentadoria'] = trabalhador['Ano_contr'] + temp_aposentadoria - nasc

print(trabalhador)
for k, v in trabalhador.items():
    print(f"{k} tem o valor: {v}")
