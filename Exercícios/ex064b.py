

n = soma = count = 0
n = int(input("Digite um número [999 para encerrar]: "))

while n != 999:
    soma += n
    count +=1
    n = int(input("Digite um número [999 para encerrar]: "))

print(f"A soma de todos os valores digitados é de: {soma}")
print(f"Foram digitados ao total: {count} números")