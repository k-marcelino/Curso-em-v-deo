'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''


times = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'Chapecoense', 'n', 'o', 'p', 'q', 'r', 's', 't')

print(f"CINCO primeiros colocados: {times[:5]}")
print(f'Último QUATRO colocados: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A chapecoense está na posição: {times.index("Chapecoense") + 1}')