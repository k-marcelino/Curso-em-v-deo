'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome='Desconhecido', gols=0):
    '''
    -> Printa o nome e quantidade de gols
    :param nome: Nome do Jogador
    :param gols: Gols marcados
    :return: Sem retorno
    '''
    print(f'O jogador {nome} fez {gols} gol(s)')


nome = str(input("Digite o nome do Jogador: "))
gols = str(input("Digite a quantidade de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
