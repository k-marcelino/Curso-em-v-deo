'''Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):
print(c)
print(‘Acabou’)'''

for i in range(0,3):
    print(f"Essa é a {i} iteração")

print('#' * 15)

for i in range(6, 0, -1):
    print(i)

print('#' * 15)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for i in range(i, f + 1, p):
    print(i)
print('Fim')