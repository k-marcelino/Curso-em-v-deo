# Crie um programa que leia o quanto de dinheiro uma pessoa tem em sua carteira e mostre quantos dólares...
# ...ela pode comprar

n = float(input("Quantos reais você tem? "))
conversor = 3.27
d = n / conversor

print("Você pode comprar US${:.2f} com esse valor".format(d))

# como importar da internet esse valor de conversor atualizado no momento que executar o programa?
