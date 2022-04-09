'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''


def leiaint(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0:31mErro! Digite um número inteiro válido\033[m")
        if ok == True:
            break
    return valor


n = leiaint("Digite um número: ")
print(f"Você digitou o número {n}")
