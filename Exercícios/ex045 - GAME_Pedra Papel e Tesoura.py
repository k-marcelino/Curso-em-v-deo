# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

lista = ['pedra', 'papel', 'tesoura']
choice = 0

print("VAMOS JOGAR JOKENPÔ!")
while choice < 1 or choice >3:
    choice = int(input("Lista de jogadas:\n"
                       "[1] PEDRA\n"
                       "[2] PAPEL\n"
                       "[3] TESOURA\n"
                       "Digite o código correspondente a sua escolha (1, 2 ou 3): "))

pc = random.choice(lista)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")

print(f"Você escolheu {lista[choice - 1]} e o computador escolheu {pc}")

if choice == 1:
    if pc == 'pedra':
        print("Jogo Empatado")
    elif pc == 'papel':
        print("Você perdeu, tente novamente")
    else:
        print("Parabéns, você venceu!")

elif choice == 2:
    if pc == 'pedra':
        print("Parabéns, você venceu!")
    elif pc == 'papel':
        print("Jogo Empatado")
    else:
        print("Você perdeu, tente novamente")

else:
    if pc == 'pedra':
        print("Você perdeu, tente novamente")
    elif pc == 'papel':
        print("Parabéns, você venceu!")
    else:
        print("Jogo Empatado")
