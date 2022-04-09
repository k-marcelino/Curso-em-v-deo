# Faça um programe que leia un número inteiro e mostre na tela o seu sucessor e antecessor

n = int(input("Digite um número: "))
antecessor = n - 1
sucessor = n + 1

print("O seu antecessor é: {} e o seu sucessor é: {}".format(antecessor, sucessor))

# ou ao invés de fazer variáveis p antecesor e sucessor, colocar a fórmula direta no .format
