# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Qual a quantidade de Km percorridos? "))
d = int(input("Qual a quantidade de dias alugados? "))

p = (60 * d) + (0.15 * km)

print(f"O carro foi alugado durante {d} dias e foram percorridos {km}km, o preço a ser pago é de R${p:.2f}")

