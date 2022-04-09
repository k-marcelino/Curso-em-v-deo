from random import randint
from time import sleep #faz o dar um delay antes de algum comando
n = randint(0, 5)
user = int(input("Vamos jogar...\nEstou pensando em um número, tente adivinhar qual!\nDica: está entre 0 e 5: "))

print("Hmmmmm...")
sleep(3) #espera 3 segundos antes da próxima linha
print("Parabéns, você é provavelmente um telepata!" if user == n else f"O número escolhido foi {n}:/ Tente novamente!")
