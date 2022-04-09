'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []

while True:
    n = int(input("Digite um valor: "))

    if n not in lista:
        print("Valor único adicionado")
        lista.append(n)
    else:
        print("Valor já existente, não pôde ser adicionado")

    exit = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
    if exit == 'n':
        break

lista.sort()
print(f'Os valores únicos digitados em ordem crescente são: {lista}')
