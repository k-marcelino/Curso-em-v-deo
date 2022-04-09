'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre
Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos
opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''


##### TEORIA
## Interactive Help

#help() # Dá pra rodar direto no console, para sair comando: quit
help(print)

# Outra maneira, ler direto a documentação interna
print(print.__doc__)
#print(input.__doc__)


## Docstrings

# Quando se coloca as três aspas na linha debaixo do def e da enter o pychamr ja cria uma estrutura padrão de docstring automaticamente
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = 1
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)

# Parâmetros Opcionais

def somar(a, b, c):
    print(f'Soma: {a + b + c}')

somar(3, 2, 5)
#somar(8, 4) # Aqui sem um valor default para os parâmetros daria erro

# Para corrigir só colocar o default como zero por exemplo
def somar(a=0, b=0, c=0):
    '''
    -> Soma os três valores e mostra o resultado na tela
    :param a: 1º valor
    :param b: 2º valor
    :param c: 3º valor
    :return: Sem retorno
    '''
    print(f'Soma: {a + b + c}')

help(somar)
somar(3, 2, 5)
somar(8, 4)
somar(3)
somar()
somar(c=3, b=2) # Dá para informar os parâmetros dessa forma, mesmo fora de ordem

## Falado brevemente sobre escopos Global e Local
#global
#local


## Retornando Valores

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

resp = somar(3, 2, 5)
print(resp)
# ou
print(somar(3, 2, 5))

#
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'Os calculos deram: {r1}, {r2} e {r3}')


##### PRÁTICA

def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input("Digite um número: "))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
