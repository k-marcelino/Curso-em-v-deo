'''Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de
repetição while no Python. Por exemplo:

c=1 while c !=10:
print(c)
c+=1
print(‘Acabou’)'''

# Difere do for quando não se sabe qual o range


'''i = 1
while i < 10:
    print(i)
    i += 1'''

#
'''n = 0
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

#
n = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')