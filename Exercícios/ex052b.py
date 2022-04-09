

n = int(input("Digite um número para verificar se é primo: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')

if count == 2:
    print(f'\n\033[mO número {n} foi divisível {count} vezes, SENDO um número primo')
else:
    print(f'\n\033[mO número {n} foi divisível {count} vezes, NÃO sendo um número primo')