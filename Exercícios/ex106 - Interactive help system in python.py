'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''

cores = {'limpa': "\033[m",
         'branco': "\033[7:30m",
         'preto': "\033[7:30m",
         'vermelho': "\033[0:30:41m",
         'verde': "\033[0:30:42m",
         'amarelo': "\033[0:30:43m",
         'azul': "\033[0:30:44m",
         'roxo': "\033[0:30:45m"}


def ajuda(function):
    help(function)

def titulo(msg, cor='limpa'):
    tam = len(msg) + 4
    print(f'{cores[cor]}', end='')
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)
    print(f'{cores["limpa"]}', end='')


comando = ''
while True:
    titulo("Sistem de ajuda PyHelp", cor='vermelho')
    comando = str(input('Função ou lib: '))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)

titulo("Até Logo!", 'branco')
