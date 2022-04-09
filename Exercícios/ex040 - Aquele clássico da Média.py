'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

print("VAMOS SABER SUA MÉDIA!\n")
n1 = float(input("Digite a primera nota: "))
n2 = float(input("Digite a segunda nota: "))

mean = (n1 + n2)/ 2

if mean < 5:
    print(f"REPROVADO! Sua média foi {mean}")
elif mean < 7:
    print(f"RECUPERAÇÃO! Sua média foi {mean}")
else:
    print(f"APROVADO! Sua média foi {mean}")
