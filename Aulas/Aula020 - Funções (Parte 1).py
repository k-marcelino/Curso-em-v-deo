'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

# Desempacotamento
def contador(*num): #vários parâmetros, sem saber quantos são
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {len(num)}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#
def dobra(lista):
    pos = 0
    while pos <len(lista):
        lista[pos] *=2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
