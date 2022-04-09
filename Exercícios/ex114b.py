# Está dando erro, jeito ensinado em aula, mas a lib deve ter sofrido alteração
# na solução do ex114 no outro arquivo está funcionando até o momento

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http//www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site {site} não está acessível no momento')
else:
    print(f'Consegui acessar o site {site} com sucesso')
    print(site.read())
