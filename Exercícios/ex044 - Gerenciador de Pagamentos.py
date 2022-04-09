'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print("Vamos calcular o valor de desconto da sua compra")
valor = float(input("Digite o valor da compra: R$"))
cod = 0

while cod < 1 or cod > 4:
    cod = int(input("[1] À vista, no dinheiro ou cheque\n"
                    "[2] À vista no cartão\n"
                    "[3] 2x no cartão\n"
                    "[4] 3x ou mais no cartão\n\n"
                    "Insira o código da condição de pagamento:"))

# daria para fazer as contas nas condições e só um print no final falando o resultado
# tb da pra pedir quantas parcelas exatamente da opção 4, e muito mais...
if cod == 1:
    print(f"O valor à vista da sua compra é de R${valor * 0.9}")
elif cod == 2:
    print(f"O valor à vista no cartão é de R${valor * 0.95}")
elif cod == 3:
    print(f"O valor total da compra parcelada é de R${valor}")
else:
    print(f"O valor total da compra parcelada é de R${valor * 1.2}")
