'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

# Variáveis
jogadores = []
jogador = {}
gols = []
exit = ' '

# Obtenção de dados
while True:
    jogador['Nome'] = str(input('Nome: '))
    # Obtenção de dados sobre partidas e gols
    jogador['partidas'] = int(input('Quantidade de partidas jogadas : '))
    for i in range(jogador['partidas']):
        n = int(input(f'Quantidade de gols na partida {i + 1} : '))
        gols.append(n)

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())

    while True:
        exit = str(input("Deseja Continuar? [S/N]: ")).strip().lower()[0]
        if exit in 'ns':
            break
        print("Erro! Digite apenas 's' ou 'n'")
    if exit == 'n':
        break

# Prints da lista completa
print(f'Lista completa: {jogadores}')

# Print tabela
print(f'cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for pos, value in enumerate(jogadores):
    print(f'{pos:>3}', end='')
    for i in value.values():
        print(f'{str(i):<15}', end='')
    print()

# Print jogador individual
while True:
    busca = int(input("Mostrar dados de qual jogador? [999] para sair: "))
    if busca == 999:
        print("Encerrado!")
        break
    if busca >= len(jogadores):
        print('Erro! Código do jogador inválido, tente novamente')
    else:
        print(f"Levantamento do jogador {jogadores[busca]['Nome']}")
        for pos, i in enumerate(jogadores[busca]['Gols']):
            print(f'   No jogo {pos} fez {i} gols')
        print('#' * 30)