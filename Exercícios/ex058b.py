
from random import randint
from time import sleep #faz o dar um delay antes de algum comando

n = randint(0, 5)
user = 0
count = 10

print("Vamos Jogar!")
while user != n:
    n = randint(0, 5)
    user = int(input("Estou pensando em um número, tente adivinhar qual!\nDica: está entre 0 e 5: "))
    count +=1

    print("Hmmmmm...")
    sleep(2) #espera 3 segundos antes da próxima linha
    print("Parabéns, você é provavelmente um telepata!" if user == n else f"O número escolhido foi {n}:/ Tente novamente!")
    print(f"Foram necessarias {count} tentativas")