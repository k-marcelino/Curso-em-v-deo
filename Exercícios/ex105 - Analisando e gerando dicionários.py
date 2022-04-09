'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''


def notas(*n, situ=False):
    '''
    -> Função para analisar várias notas e situações de vários alunos
    :param num: Uma ou mais notas do aluno
    :param situ: Opcional, indica se deve ou não adicionar a situação
    :return: Dicionário com as informçações
    '''
    r = {}
    r['qt'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = round(sum(n)/r['qt'], 2)
    if situ:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


notas(5.5, 7.2, 8.0, 9.2, 7.8, situ=True)
print(notas)
#help(notas)
