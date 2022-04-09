'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes '''

print("Vamos analisar se podemos formar um triângulo!\n")
s1 = float(input("Digite o comprimento do primeiro segmento: "))
s2 = float(input("Digite o comprimento do segundo segmento: "))
s3 = float(input("Digite o comprimento do terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Com esses segmento É possível formar um triângulo!")

    #if s1 == s2 == s3: (python tb deixar fazer desse jeito!
    if s1 == s2 and s1 == s3:
        print("Esse é um triângulo equilátero (todos os lados iguais)")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Esse é um triângulo isósceles (dois lados iguais)")
    else: #daria para colocar condição if s1 != s2 != s3 != s1:
        print("Esse é um triângulo escaleno (todos os lados diferentes")

else:
    print("Com esses segmentos NÃO é possível formar um triângulo!")