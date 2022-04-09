'''Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os
seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.'''

#Estrutura: entre a abertura do colchete e o "m" podem ter 0,1,2 ou 3 códigos, todos são opcionais

#\033[1º: Estilo, 2º: Texto, 3º: Background   m

#Padrão ANSI
#Códigos - Stilo:
#0: Nenhum
#1: Negrito
#4: Sublinhado
#7: Cores invertidas

#Códigos - Cores e Background a ordem é igual, mas backgroun vai do código 40 a 47:
#30: Branco
#31: Vermelho
#32: Verde
#33: Amarelo
#34: Azul
#35: Magenta
#36: Ciano
#37: Cinza



#Exemplo
#\033[0;33;44m
# Colocando \033[m no final do texto ele volta a formatação padrão para o restante
print("\033[0;30;41mTESTE")
print("\033[0;30;41mTESTE\033[m")
print("\033[4;33;44mTESTE")
print("\033[4;33;44mTESTE\033[m")
print("\033[1;35;43mTESTE")
print("\033[1;35;43mTESTE\033[m")
print("\033[30;42mTESTE")
print("\033[30;42mTESTE\033[m")
print("\033[mTESTE")
print("\033[mTESTE\033[m")
print("\033[7;30mTESTE")
print("\033[7;30mTESTE\033[m")

#Dá pra criar um dicionário para organizar melhor como usar essas cores
cores = {'limpa': "\033[m",
         'branco': "\033[30m",
         'vermelho': "\033[31m",
         'verde': "\033[32m",
         'amarelo': "\033[33m",
         'azul': "\033[344m",
         'magenta': "\033[35m",
         'ciano': "\033[36m",
         'cinza': "\033[37m"}

n = input("Digite seu nome: ")
print(f"Olá, {cores['vermelho']}{n}{cores['limpa']} é um prazer recebê-lo")
