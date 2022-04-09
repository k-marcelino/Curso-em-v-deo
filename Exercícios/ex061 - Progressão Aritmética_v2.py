'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

t = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da pa: "))

i = 1
answer = t
while i <= 10:
    print(f'{answer} 👉 ', end = '')
    answer += r
    i += 1

print("Fim")
