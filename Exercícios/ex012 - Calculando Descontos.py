#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

n = float(input("Digite o valor base do produto antes do desconto: R$"))
desconto = 5

print("O valor de R${:.2f} com desconto de {}% é de: R${:.2f}".format(n, desconto, n* (1 - (desconto / 100))))
