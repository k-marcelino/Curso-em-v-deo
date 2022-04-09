'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.'''

# Variáveis
jogador = {}
gols = []

jogador['Nome'] = str(input('Nome: '))
# Obtenção de dados sobre partidas e gols
partidas = int(input('Quantidade de partidas jogadas : '))
for i in range(partidas):
    n = int(input(f'Quantidade de gols na partida {i + 1} : '))
    gols.append(n)

jogador['Gols'] = gols
jogador['Total'] = sum(gols)

# Prints do dicionário
print(f'Dicinário completo: {jogador}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')

# Prints finais
print(f'\nO jogador {jogador["Nome"]} jogou {partidas} partidas')
for i, n in enumerate(gols):
    print(f"Na partida {i + 1}, fez {n} gols")

print(f"Foi um total de {jogador['Total']} gols")
