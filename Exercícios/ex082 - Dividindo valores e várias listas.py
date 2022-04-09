'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
even = []
odd = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

    exit = str(input("Deseja continuar acrescentando? [S/N]: ")).strip().lower()[0]
    if exit == 'n':
        break

print(f'\nLista completa: {lista}')
print(f'Lista de pares: {even}')
print(f'Lista de ímpares: {odd}')