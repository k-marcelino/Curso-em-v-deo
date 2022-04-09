import random
import emoji
#números aleatórios (float) de zero até um
n = random.random()
#números aleatórios inteiros de 1 até 10, ou o que for configurado
n1 = random.randint(1, 10)

print(n, n1)
print(emoji.emojize("Olá, mundo :blush:", use_aliases=True))