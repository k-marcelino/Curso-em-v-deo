'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo. '''

while True:
    n = int(input("Digite um número para saber sua tabuada: "))
    if n < 0:
        print("Programa Encerrado")
        break
    print("-" *15)

    for i in range(1, 11): # dava pra usar while tb
        print(f"{n} x {i} = {i * n}")
