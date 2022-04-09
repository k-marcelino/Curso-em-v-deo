'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

words = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
         'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input("Digite um número entre 0 e 20 (Para sair digite um número fora do range): "))
    if n < 0 or n > 20:
        break
    print(f'Você digitou {words[n]}')

print("Fim de Programa")
