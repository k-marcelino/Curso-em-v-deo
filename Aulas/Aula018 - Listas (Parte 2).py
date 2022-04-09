'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.'''



dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = []
# Criando uma lista e adicionando listas dentro
pessoas.append(dados[:])
print(pessoas)
pessoas.append(['Maria', 19])
print(pessoas)
pessoas.append(['João', 32])
print(pessoas)

#ou
pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas2)

#
print(pessoas[1])
print(pessoas[0][0])
print(pessoas[1][1])

### Prática

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

# Quando faz um append desse jeito está criando uma ligação entre as estruturas e não apenas uma cópia
galera = []
galera.append(teste)
print(galera)

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste)
print(galera)

# Para fazer uma cópia é necessário usar o slicing [:].Ex:
galera.append(teste[:])
