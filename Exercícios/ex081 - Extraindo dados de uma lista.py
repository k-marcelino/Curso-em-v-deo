'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    n = int(input("Digite um número: ")) # daria pra colocar append direto sem armazenar em n
    lista.append(n)

    exit = str(input("Deseja continuar acrescentando? [S/N]: ")).strip().lower()[0]
    if exit == 'n':
        break

print(f'\nNúmeros Digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista Ordenada de forma decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista')
else:
    print("O valor 5 não foi digitado")
