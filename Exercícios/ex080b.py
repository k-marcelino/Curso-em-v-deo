'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a
lista ordenada na tela.'''

# Inicializando lista
lista = []

# Coletando os valores para lista
for i in range(5):
    n = int(input("Digite um valor: "))
    # Se é o primeiro número é adicionado usando append
    if len(lista) == 0:
        lista.append(n)
        print(f'O valor {n} foi inserido na posição {lista.index(n)}')
    # A partir do segundo número entra nessa condição:
    else:
        # Loop para checar, se o valor digitado for menor que o atual, então ele toma seu lugar e desloca a lista para a direita
        for pos, value in enumerate(lista):
            if n < value:
                lista.insert(pos, n)
                print(f'O valor {n} foi inserido na posição {pos}')
                break
            # Condição para suprir o maior número adicionado,
            # Se chegou ao final da lista e não é menor que nenhum número, então o valor digitado assume a última posição
            elif pos == len(lista) - 1:
                lista.insert(pos + 1, n)
                print(f'O valor {n} foi inserido na posição {pos + 1}')
                break

# Resposta final ordenada
print(f'O valores digitados em ordem foram: {lista}')
