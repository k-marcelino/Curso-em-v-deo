# Resolução Guanabara

expr = str(input("Digite a expressão: "))
pilha = []

for char in expr:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(char)
            break

if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')