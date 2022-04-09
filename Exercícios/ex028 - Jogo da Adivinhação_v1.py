'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

n = 2
user = int(input("Vamos jogar...\nEstou pensando em um número, tente adivinhar qual!\nDica: está entre 0 e 5: "))

#if user == n:
#    print("\nParabéns, você é provavelmente um telepata!")
#else:
#    print("\n:/ Tente novamente!")

#ou usar a condição simplificadada, o "operador ternário" do python
#também da pra usar random() na hora de definir o "n"

print("\nParabéns, você é provavelmente um telepata!" if user == n else "\n:/ Tente novamente!")