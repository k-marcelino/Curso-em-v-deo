'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os
dados em forma tabular.'''

prod_price = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
              'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livros', 34.90)

for pos in range(len(prod_price)):
    if pos % 2 == 0:
        print(f'{prod_price[pos]:.<30} R${prod_price[pos+1]:>8.2f}')
