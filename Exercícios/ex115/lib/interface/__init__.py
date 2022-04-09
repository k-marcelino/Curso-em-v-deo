

def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print("\033[0:31mErro! Digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print('\033[0:31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha)
    print(txt.center(42))
    print(linha)


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for pos, item in enumerate(lista):
        print(f'\033[33m{pos + 1}\033[m - \033[34m{item}\033[m')
    print(linha)

    opc = leiaint('\033[032mSua Opção: \033[33m')
    return opc
