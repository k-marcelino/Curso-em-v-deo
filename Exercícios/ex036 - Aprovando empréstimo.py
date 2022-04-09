'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

v_casa = int(input("Digite o valor da casa: R$"))
v_salario = int(input("Digite o valor do seu salário: R$"))
anos = int(input("Digite em quantos anos a casa será paga: "))

meses = anos * 12
prest = v_casa / meses

print(f"O valor da prestação é de R${prest:.2f}, a serem pagos em {meses} meses")


if prest <= (v_salario * 0.30):
    print("Seu empréstimo foi APROVADO")
else:
    print("Seu empréstimo foi RECUSADO")
