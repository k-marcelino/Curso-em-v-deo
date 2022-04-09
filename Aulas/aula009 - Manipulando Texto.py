
frase = "Curso em Vídeo Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print("""A frase
pode  ser escrita
em diferentes linhas 
desse jeito""")

#print(frase.translate())
print(len(frase))
#count()
#find()

print('Curso' in frase)
print(frase.find('vídeo')) #se mostrar '-1' é porque não existe
print(frase.lower() .find('vídeo'))
#frase.replace('vai sair', 'vai entrar')
#frase.upper()
#frase.lower()
#frase.capitalize()
#frase.title()
#frase.strip()
#frase.rstrip()
#frase.lstrip()

#pesquisar mais\//

print(frase.split())

split = (frase.split())
print(split[0])
print(split[2][3])

'-'.join(frase)