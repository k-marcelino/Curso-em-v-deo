'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da pa: "))
answer = primeiro
i = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while i <= total:
        print(f'{answer} 👉 ', end = '')
        answer += r
        i += 1
    print("Pausa")

    mais = int(input("Quantos termos você quer mostrar a mais?: "))

print(f'Progressão finalizada com {total} termos')