'''Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

n = str(input("Digite um ano para saber se o mesmo é bissexto: "))

# se os dois últimos dígitos forem = 0 entra na primeira condição, senão entra no else
if n[2:] == 00:
    print(f"O ano {n} é bissexto" if int(n) % 4 == 0 else f"O ano {n} não é bissexto!")
else:
    print(f"O ano {n} é bissexto" if int(n) % 400 == 0 else f"O ano {n} não é bissexto!")
