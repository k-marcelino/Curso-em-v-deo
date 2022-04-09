'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from operator import itemgetter
dados = {}
ranking = []

# Gerando números aleatórios e armazenando no dicionário
print("Valores Sorteados: \n")
for i in range(0, 4):
    dados[f'Jogador{i + 1}'] = randint(1, 6)
    print(f'O Jogador{i + 1} tirou {dados[f"Jogador{i + 1}"]}')

# Comando para ordenar valores do dicionário em ordem decrescente
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

# Print final
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
