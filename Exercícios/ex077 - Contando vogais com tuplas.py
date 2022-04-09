'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

words =('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
        'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in words:
    vogal = ' '
    for letra in palavra:
        if letra in 'AEIOU':
            vogal += letra + ' '

    print(f'Na palavra {palavra:<11} temos as vogais: {vogal.strip().lower()}')
