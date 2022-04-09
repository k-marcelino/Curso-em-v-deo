'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.'''

lanches = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']
print(lanches)
lanches.pop()
# .insert(posição, valor a ser acrescentado)
# .append()
# del()
# .pop()
# .remove()
# .clear()

# Criando listas com range
valores = list(range(4, 11))
print(valores)

# Criação manual de listas
valores = [8, 2, 5, 4, 9, 3, 0]

# Ordenar Valores
valores.sort()
print(valores)
# Ordenar na ordem inversa
valores.sort(reverse=True)
print(valores)
# Tamanho da lista
print(len(valores))


### Parte Prática da aula ###

# Criação da lista
num = [2, 5, 9, 1]
print(num)
# Mudando o valor na posição 2
num[2] = 3
print(num)
# Incluindo um elemento no final da lista
num.append(7)
print(num)
# Ordenando a lista em ordem crescente
num.sort()
print(num)
# Ordenando a lista em ordem decrescente
num.sort(reverse=True)
print(num)
# Inserindo um número na lista, dessa forma desloca os outros
num.insert(2, 0)
print(num)
# Removendo último elemento
num.pop()
print(num)
# Removendo de acordo com o elemento e não posição (caso tenha duplicado, só elimina o primeiro que achar)
num.remove(2)
print(num)

###

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Se alterar um elemento na segunda lista, também muda na original (o python faz uma ligação entre elas)
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Tem como fazer uma cópia da lista para isso não ocorrer - usando slicing
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')