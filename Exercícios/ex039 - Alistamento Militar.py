'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de
se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.'''

from datetime import date

# extrai o ano de acordo com o sistema do computador
ano = date.today().year
alist = 18

nasc = int(input("Digite o seu ano de nascimento no formato (aaaa): "))
idade = ano - nasc

if idade <= alist:
    print(f"Ainda faltam {alist - idade} anos para se alistar no serviço militar")
elif idade == alist:
    print("Está na hora de se alistar no serviço mililtar")
else:
    print(f"Você tem {idade} anos e está atrasado para se alistar no serviço militar em {idade - alist} anos")
