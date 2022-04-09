'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0, 10)
acertou = False
count = 0

print("Vamos Jogar!")
while not acertou:
    user = int(input("Estou pensando em um número, tente adivinhar qual!\nDica: está entre 0 e 10: "))
    count +=1
    if user == computador:
        acertou = True
    elif user < computador:
        print("Mais... Tente Novamente!")
    elif user > computador:
        print("Menos... Tente Novamente!")

print("Parabéns, você é provavelmente um telepata!")
print(f"Foram necessarias {count} tentativas")