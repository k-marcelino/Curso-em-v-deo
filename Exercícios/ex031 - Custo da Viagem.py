'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km =200
distance = int(input("Digite a distância que será percorrida na viagem: "))

if distance <= km:
    p = float(distance * 0.50)
    print(f"A sua viagem custará R$0.50 por Km totalizando R${p:.2f}")
else:
    p = float(distance * 0.45)
    print(f"A sua viagem custará R$0.45 por Km totalizando R${p:.2f}")
