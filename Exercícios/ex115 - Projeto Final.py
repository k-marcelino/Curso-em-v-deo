
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'ex115_database.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Mostra o conteúdo no arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastra nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mDigite uma opção válida\033[m')
    sleep(2)
