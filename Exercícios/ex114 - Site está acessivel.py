'''Exercício Python 114: Crie um código em Python que teste se o site pudim está
acessível pelo computador usado.'''

import urllib
import urllib.request
site = str(input('Insira o site: '))
try:
    site1 = urllib.request.urlopen('https://www.'+site+'/')
except urllib.request.URLError:
    print('\033[0:31mO Site não está acessível no momento\033[m')
else:
    print('Consegui abrir o site com sucesso!')
