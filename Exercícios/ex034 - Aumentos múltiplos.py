'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.  Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input("Digite o salário do funcionário a ter aumento: R$"))

print(f"O novo salário é de R${salario * 1.15:.2f}" if salario <= 1250 else f"O novo salário é de R${salario * 1.10:.2f}")
