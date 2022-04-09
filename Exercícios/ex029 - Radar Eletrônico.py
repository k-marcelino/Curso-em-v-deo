'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

limite = 80
custo = 7

velocidade = int(input("Escreva a velocidade do carro em Km/h: "))
multa = (velocidade - limite) * custo

#print("\nVocê está dentro da velocidade" if velocidade <= limite else f"\nVocê passou da velocidade limite, a sua multa é de R${multa}")
if velocidade < limite:
    print("Tenha uma boa viagem, você está dentro da velocidade limite")
else:
    print(f"Você está acima do limite permitido!! Você foi multado em R${multa:.2f}")
