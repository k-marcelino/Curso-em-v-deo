'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n=1, show=False):
    '''
    -> Calcula fatorial de um número
    :param n: Número a ser calculado
    :param show: Se True será mostrado os cálculos, de forma análoga 'False' não mostra
    :return: Retorna o fatorial de "n"
    '''
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i} ', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5, show=False))
print(fatorial(5, show=True))
