#Escreva um program que converta uma temperatura digitada em Cº para Fº.

temp = float(input('Digite a temperatura em Cº: '))
nova_temp = (temp * (9/5)) + 32

print("A temperatura de {}ºC equivale a {}ºF".format(temp, nova_temp))