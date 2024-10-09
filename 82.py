lista = list()
dados = list()
count = 0
n = "s"
maior = menor = 0
while n in "s":
    dados.append(str(input("nome: ")))
    dados.append(float(input("peso: ")))
    if len(dados) == 0:
        maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < maior:
            menor = dados[1]
    lista.append(dados[:])
    n = str(input("DESEJA CONTINUAR? ")).strip().lower()[0]
    count += 1
    dados.clear()
print(f"foram analisadas {count} pessoas")
for p in lista:
    if p[1] == maior:
        print(f"as mais pesadas foram {p[0]} com {maior}KG")
    if p[1] == menor:
        print(f"as mais leves foram {p[0]} com {menor}KG")
