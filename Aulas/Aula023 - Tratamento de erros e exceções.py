'''Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
Aprenda como usar a estrutura try except no Python de uma forma simples.'''

##### TEORIA
'''
print(x) # sem ter declarado a variável antes

# Esse erro é na verdade chamado de 'exceção'

#
n = int(input('Número: ')) # Exceção de value error caso digite qualquer coisa que não seja um número

#
a = 8
b = 0

r = a/b # Exceção de denominador zero
# outro exemplo
r = 2/'2' # TypeError

#
lst = [3, 6, 4]
print(lst[3]) # Out of range

#
#Importar módulo que não existe # Module Not Found Error

#
# Enfim, têm inúmeros, para ver mais procurar "Python list of exceptions:

'''
##### PRÁTICA
'''
try: # Operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as error: # Falha
    print(f'Infelizmente tivemos um problema :/\n Erro encontrado: {error.__class__}')
    # Têm vários métodos depois do 'error.', por exemplo valor, classe, contexto...
else: # Deu certo
    print(f'O resultado é {r}')
finally: # Certo/ Falha - sempre vai acontecer
    print('Volte Sempre')
'''
# Else e Finally são opcionais!
# Pode se expandir e ter vários except na estrutura, cada um com sua própria mensagem e tratamento

try: # Operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError): # Falha
    print(f'Houve um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário não informar os dados')
except Exception as error: # Falha
    print(f'Infelizmente tivemos um problema :/\n Erro encontrado: {error.__cause__}')
else: # Deu certo
    print(f'O resultado é {r:.2f}')
finally: # Certo/ Falha - sempre vai acontecer
    print('Volte Sempre!')

