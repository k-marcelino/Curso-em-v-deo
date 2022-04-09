'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.'''

print("Vamos analisar se podemos formar um triângulo!\n")
s1 = float(input("Digite o comprimento do primeiro segmento: "))
s2 = float(input("Digite o comprimento do segundo segmento: "))
s3 = float(input("Digite o comprimento do terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Com esses segmento É possível formar um triângulo!")
else:
    print("Com esses segmentos NÃO é possível formar um triângulo!")
