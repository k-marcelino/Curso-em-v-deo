
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
