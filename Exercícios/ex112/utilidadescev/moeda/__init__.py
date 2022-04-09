
def aumentar(n, aumento=1, moeda=False):
        resp = n * (1 + aumento/100)
        return resp if moeda is False else coin(n)


def diminuir(n, reduzir=1, moeda=False):
    if moeda:
        return coin(n * (1 - reduzir/100))
    else:
        return n * (1 - reduzir/100)


def dobro(n, moeda=False):
    if moeda:
        return coin(n * 2)
    else:
        return n * 2


def metade(n, moeda=False):
    if moeda:
        return coin(n/2)
    else:
        return n / 2


def coin(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(valor=0, tx_aumento=10, tx_redu=5):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{coin(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'{tx_aumento}% de aumento: \t{aumentar(valor, tx_aumento, True)}')
    print(f'{tx_redu}% de redução: \t{diminuir(valor, tx_redu, True)}')
    print('-' * 30)
