'''Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os
comandos if.. elif.. else em programas Python. '''
import unidecode

lista_fem = ['ana', 'julia', 'jessica']
lista_masc = ['rodrigo', 'tiago', 'gustavo']

nome = str(input("Qual é o seu nome? ")).lower()
# Função unidecode tira todos os acentos do nome
name = unidecode.unidecode(nome.lower())

if name == "kevyn":
    print("Seu nome é lindão!")
elif name == 'pedro' or name == 'maria':
    print("Seu nome é bem popular")
elif name in lista_fem:
    print("Belo nome feminino,")
elif name in lista_masc:
    print("Belo nome masculino,")
else:
    print("Seu nome é bem normal,")

print(f"Tenha um bom dia, {nome}!")







