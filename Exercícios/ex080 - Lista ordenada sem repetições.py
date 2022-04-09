'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a
lista ordenada na tela.'''

# Código primeiro recebe todos os números e depois faço um sort algorithm para ordenar
# a proposta do exercício inicial era já acrescentar o número direto na posição ideal, fiz na resolução "b"

# Inicializando lista
lista = []

# Coletando os valores para lista
for i in range(5):
    n = int(input("Digite um valor: "))
    lista.append(n)

# Algoritmo de ordenação simples
# Loop infinito só sera interrompido quando a variável de controle "change" não detectar mais nenhuma mundança
while True:
    change = 0
    swap = 0
    # Percorre a lista
    for pos, valor in enumerate(lista):
        # Se a próxima posição não fugir do range da lista e o valor atual for maior que o próximo valor da lista
        # então trocam de lugar, usando a variável "swap" como intermediário
        if (pos + 1) < len(lista) and valor > lista[pos + 1]:
            swap = lista[pos + 1]
            lista[pos + 1] = lista[pos]
            lista[pos] = swap
            # change diz se foi feita alguma alteração durante o loop
            change +=1
    # Se não, interrompe o loop infinito
    if change == 0:
        break

print(f'O valores digitados em ordem foram: {lista}')
