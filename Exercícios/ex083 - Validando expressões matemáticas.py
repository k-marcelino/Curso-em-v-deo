'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

# Não está dando certo quando não tem parêntese na resposta, estranho
n = list(input("Digite a expressão matemática: "))

if '(' or ')' in n:
    if n.count('(') == n.count(')'):
        print('A expressão é válida')
    else:
        print("A expressão é inválida")
else:
    print('A expressão não possui parênteses, mas é válida')