

lista = []
soma = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}º número inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        soma += n

print(f'Os números fornecidos foram: {lista}')
print(f'A soma dos números pares fornecidos é: {soma}')