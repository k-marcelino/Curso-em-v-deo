'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para
hexadecimal. '''

choice = 0

n = int(input("Digite um número inteiro: "))
b = bin(n)
o = oct(n)
x = hex(n)

print("\n[1] = Binário")
print("[2] = Octal")
print("[3] = Hexadecimal")
print("[4] = todas")
while choice < 1 or choice > 4:
    choice = int(input("De acordo com a legenda, escolha uma base a ser usada para conversão: "))

if choice == 1:
    print(f'{n} em binário é igual a: {b[2:]}')
elif choice == 2:
    print(f'{n} em octal é igual a: {o[2:]}')
elif choice == 3:
    print(f'{n} em hexadecimal é igual a: {x[2:]}')
elif choice == 4:
    print(f'{n} em binário é igual a: {b[2:]}')
    print(f'{n} em octal é igual a: {o[2:]}')
    print(f'{n} em hexadecimal é igual a: {x[2:]}')
