from datetime import date
atual = date.today().year
i = 0
v = 0
for c in range(1, 7+1):
    data = int(input("digite o ano de nascimento abaixo:"))
    ano = atual - data
    if ano >= 21:
        v += 1
    else:
        i += 1
print("das {} pessoas analisadas, {} sao maiores de idade e {} sao menores de idade".format(c,v,i))