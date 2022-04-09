'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar
módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender também como
agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.'''

# Criado o python package uteis(pacote) e dentro outros pacotes ou módulos
from uteis import números

num = int(input("Digite um número: "))
fat = números.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {números.dobro(num)}")