#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input("Digite um valor em metros a ser convertido: "))

cent = n * 100
mili = n * 1000

print("{} m é igual a {} centímetros;\nE igual a {} milímetros.".format(n, cent, mili))
