from random import randint

# 1. Qual é a principal diferença dos dicionários em Python em relação às tuplas e listas.
# R: Em dicionários os índices podem ser nomeados

# 2. Considere a lista num = [8, 2, 4, 2, 5, 2] declarada em Python.
# Como vamos descobrir quantas vezes o número 2 foi cadastrado no total?
num = [8, 2, 4, 2, 5, 2]
print(num.count(2))

# 3. Em que local vamos escrever o texto que vai servir como DOCSTRINGS de uma determinada função?
# R: depois da linha de declaração da função, abaixo da linha def

# 4. Qual das estruturas compostas do Python é tida como "imutável"?
# R. Tuplas

# 5. Considere uma tupla pontos, com 20 elementos numéricos.
# Como podemos mostrar todos os valores armazenados em ordem crescente?
pontos = []
for i in range(0, 20):
    pontos.append(randint(0, 50))
print(pontos)
pontos = tuple(pontos)
print(sorted(pontos))

# 6. O comando val = list(range(1, 5)) vai criar uma variável Python com que valor?
val = list(range(1, 5))
print(val)

# 7. Para declarar uma tupla, delimitamos os valores entre os símbolos de ____.
# Para as listas, usamos ____ para delimitar os valores.
# Os dicionários usam símbolos  ____ para representar os valores.
# Das opções abaixo, qual delas é a opção que completa as lacunas na ordem?
# R: (); []; {}

# 8.  Considere a tupla letras = ('J', 'X', 'M', 'O', 'A', 'K') declarada em Python.
# Como vamos descobrir em que posição está a letra 'A'?
letras = ('J', 'X', 'M', 'O', 'A', 'K')
print(letras.index('A'))

# 9. Considere uma tupla chamada países que tem vários elementos.
# Como fazemos para mostrar o primeiro e o último elemento dessa tupla?
# R: print(países[0], países[-1])

# 10. Considere a lista num = [6, 2, 1, 4, 3] declarada em Python.
# Se quisermos ordenar os valores armazenados em num de forma decrescente, usaremos o comando:
num = [6, 2, 1, 4, 3]
num.sort(reverse=True)
print(num)
