'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

n = soma = count = maior = menor = 0
answer = 's'

while answer != 'n':
    n = int(input("Digite um número: "))
    soma += n
    count += 1
    if count == 1:
        menor = n

    maior = max(maior, n)
    menor = min(menor, n)
    answer = str(input("Você quer continuar? [S/N]: ")).lower().strip()

print(f"A média de todos os valores digitados é de: {soma/ count}")
print(f"O maior de todos os valores digitados foi: {maior}")
print(f"O menor de todos os valores digitados foi: {menor}")
print(f"Foram digitados ao total: {count} números")