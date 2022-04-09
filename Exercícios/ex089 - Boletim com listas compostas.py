'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.'''

lista = []
swap = []
count = 1

while True:
    swap.append(str(input(f"Nome: ")))
    swap.append(float(input(f"Nota {count}: ")))
    swap.append(float(input(f"Nota {count + 1}: ")))

    lista.append(swap[:])
    swap.clear()
    exit = str(input("Deseja continuar? [S/N]: ")).strip().lower()[0]
    if exit == 'n':
        break

print(f"{'Boletim':-^30}")
print('Nº:' + ' ' * 2 +'Nome:' + ' ' * 16 + 'Média:')
for pos, i in enumerate(lista):
    print(f'{pos:<5}{i[0]:<20} {(sum(i[1:]))/2}')

while True:
    n = int(input("\nMostrar a nota de qual aluno? [999] para interromper: "))
    if n == 999:
        break

    if n < len(lista):
        print(lista[n])
    else:
        print("Esse aluno não está cadastrado")