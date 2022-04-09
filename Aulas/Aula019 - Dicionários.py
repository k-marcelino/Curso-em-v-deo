'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.'''

dados = dict()
# ou
dados = {}
#
dados = {'Nome': 'Pedro',
         'Idade': 25}
print(dados)
dados['Sexo'] = 'M'
print(dados)
del dados['Idade']
print(dados)

###
filme = {'Título': 'Star Wars',
         'Ano': 1977,
         'Diretor': 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

#
filme2 = {'Título': 'Avengers',
         'Ano': 2012,
         'Diretor': 'Joss Whedon'}

filme3 = {'Título': 'Matrix',
         'Ano': 1999,
         'Diretor': 'Wachowski'}

locadora = [filme, filme2, filme3]
for i in locadora:
    print(i)

print(locadora[0]['Ano'])
print(locadora[2]['Título'])

############################
print(f'\n{" Prática ":#^50}\n')

pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 26}
print(pessoas)
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#del pessoas['Sexo']
#print(pessoas)
pessoas['Peso'] = 80
print(pessoas)

############################
print(f'\n{"#":#^30}\n')

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['UF'])
print(brasil[1]['Sigla'])

############################

estado = {}
brasil = []

for i in range(0,3):
    estado['UF'] = str(input("Digite a Unidade Federativa: "))
    estado['Sigla'] = str(input("Digite a sigla do Estado: "))
    brasil.append(estado.copy())
for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')
