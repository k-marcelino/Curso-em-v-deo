from datetime import date

n = int(input("Digite um ano para saber se o mesmo é bissexto (Coloque 0 para usar o ano atual:  "))
if n == 0:
    n = date.today().year

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f"O ano {n} é bissexto")
else:
    print(f"O ano {n} não é bissexto!")
