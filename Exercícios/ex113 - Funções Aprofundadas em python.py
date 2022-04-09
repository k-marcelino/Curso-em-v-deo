'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

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

def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print("\033[0:31mErro! Digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print('\033[0:31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n



n = leiaint("Digite um número inteiro: ")
f = leiaint("Digite um número real: ")
print(f"O número inteiro foi {n} e o número real {f}")
