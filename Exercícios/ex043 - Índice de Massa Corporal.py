'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida '''

print("CÁLCULO DO ÍNDICE DE MASSA CORPORAL")
p = float(input("Insira seu peso (em kilogramas): "))
a = float(input("Insira sua altura (em metros): "))

imc = p / (a ** 2)

if imc <= 18.5:
    print(f"Seu IMC é de {imc:.2f}, seu peso está abaixo do ideal")
elif imc <=25:
    print(f"Seu IMC é de {imc:.2f}, seu peso está normal")
elif imc <= 30:
    print(f"Seu IMC é de {imc:.2f}, o que indica sobrepeso")
elif imc <= 40:
    print(f"Seu IMC é de {imc:.2f}, o que indica obesidade")
else:
    print(f"Seu IMC é de {imc:.2f}, o que indica obesidade mórbida")
