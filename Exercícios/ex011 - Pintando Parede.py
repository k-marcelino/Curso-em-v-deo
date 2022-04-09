#Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade
# de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Qual a largura da parede? (em metros): "))
altura = float(input("Qual a altura da parede? (em metros): "))

area = largura * altura
rendimento = 2

print("A área da parede é de: {:.2f}m² e a quantidade necessária de tinta para preenchê-la é de {:.2f} l".format(area, area/rendimento))
