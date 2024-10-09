lista = list()
dicionario = dict()
n = "s"
soma = 0
while n == "s":
    dicionario["nome"] = str(input("nome: "))
    dicionario["sexo"] = str(input("sexo: "))[0]
    while dicionario["sexo"] not in "FfMm":
        print("sexo não reconhecido, tente novamente: ")
        print("")
        dicionario["sexo"] = str(input("sexo: "))[0]
    dicionario["idade"] = int(input("idade: "))
    soma += dicionario["idade"]
    lista.append(dicionario.copy()) 
    n = str(input("DESEJA CONTINUAR? ")).strip().lower()[0]
    while n not in "sn":
        print("esta palavra é invalida. tente novamente:")
        print("")
        n = str(input("DESEJA CONTINUAR? ")).strip().lower()[0]
media = (soma / len(lista))
for c in lista:
    if c["idade"] >= media:
        print(f"{c["nome"]}",end=" ")
    print(f"esta acima da media com",end=" ")
    print(f"{c["idade"]}",end=" ")
    print("anos")
print(f"a media foi {media:.2f} anos")
print(f"foram cadastradas {len(lista)} pessoas")
print("as mulheres desta lista sao: ",end=" ")
for i in lista:
    if i["sexo"] in "fF":
        print(f"{i["nome"]}",end="; ")