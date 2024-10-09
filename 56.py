mediaidade = 0
maior = 0
menor = 0
totmulher = 0
nomemaior = ()
for c in range(1, 4+1):
    print("----------------------------------")
    nome = str(input("digite o nome da {} pessoa: ".format(c))).strip()
    idade = int(input("digite a idade da {} pessoa: ".format(c)))
    mediaidade += idade
    media = mediaidade / 4
    sexo = str(input("digite o sexo da {} pessoa: [M/F] ".format(c))).lower().strip()
    if sexo == "M" or sexo == "m" and c == 1:
        nomemaior = nome
        idademaior = idade
    if idade > idademaior:
        nomemaior = nome
    if sexo == "F" or sexo == "f" and idade < 20:
        totmulher += 1
print("------------------------------------------")
print("o homem mais velho se chama {}".format(nomemaior))
print("------------------------------------------")
print("a media de idade do grupo foi de {:.1f} anos".format(media))
print("------------------------------------------")
print("{} mulheres tem menos de 20 anos".format(totmulher))