'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. '''

# Não tirei acentuação, mas dá pra colocar

# Exemplos de Palavras:
palindromos = ['ama', 'ararara', 'ele', 'mirim', 'ovo', 'radar']

# Exemplos de frases:
'''
A base do teto desaba
A cara rajada da jararaca
Acuda cadela da Leda caduca
A dama admirou o rim da amada
A Daniela ama a lei? Nada
Adias a data da saída
A diva em Argel alegra - me a vida
A droga do dote é todo da gorda
'''

n = str(input('Verifique se a frase é um palíndromo: '))
frase = ''.join(char for char in n if char.isalnum()).lower()
print(frase)
opposite = ''

for i in range(len(frase) -1, -1, -1):
    opposite += frase[i]

if frase == opposite:
    print(f'A frase é um palíndromo')
else:
    print(f'A frase não é um palíndromo')