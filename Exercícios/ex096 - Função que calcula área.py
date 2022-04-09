'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(): # Ou daria para colocar como argumentos
    largura = int(input("Largura do Terreno (m): "))
    comprimento = int(input("Comprimento do Terreno (m): "))
    print(f"Área do terreno: {largura * comprimento} m²")


area()
