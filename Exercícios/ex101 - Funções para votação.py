'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano_nasc):
    '''

    :param ano_nasc: Ano de nascimento da pessoa
    :return: Retorna se a pessoa tem voto "Negado", "Opcional ou "Obrigatório nas eleições
    '''
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano_nasc

    if idade > 0 and idade < 16:
        return f'Com {idade} anos o voto é: NEGADO'
    elif idade >=16 and idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é: OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos o voto é: OBRIGATÓRIO'

print(voto(2000))
print(voto(2006))
print(voto(2010))
print(voto(1900))
