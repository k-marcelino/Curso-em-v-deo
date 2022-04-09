#Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

n = float(input("Digite o salário do funcionário que ganhará o aumento: R$"))
fator = 1.15

print("O novo salário é de: R${:.2f}".format(n * fator))
