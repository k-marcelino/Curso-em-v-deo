'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma
estrutura, acessíveis por chaves individuais.'''

# Pode ser sem os parênteses
lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanches[0])

# Tuplas são imutáveis
#lanches[1] = Pizza

# Primeiro jeito de iterar
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posição {cont}')

print('_-' * 15)
# Segundo jeito de iterar
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

# Ordenado
print(sorted(lanches))

# Concatenando
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # (a + b) é diferente de (b + a)
print(c)

# Propriedades
print(c.count(5)) # Contar elementos dentro da tupla
print(c.index(8)) # Que posição está esse elemento (se tiver elemento duplicado ele retorna apenas o 1º)

# Tuplas aceitam mais de um tipo de estrutura
pessoa = ('Gustavo', 39, 'M', 100)
print(pessoa)

# Apagar (apaga na memória)
del(pessoa)
print(pessoa)