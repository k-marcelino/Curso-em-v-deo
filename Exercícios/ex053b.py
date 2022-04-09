'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

n = str(input('Verifique se a frase é um palíndromo: ')).strip().upper()
palavras = n.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print(f'A frase é um palíndromo')
else:
    print(f'A frase não é um palíndromo')