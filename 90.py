lista = dict()
lista1 = list()
n = "s"
tot = 0
dados = 0
while n == "s":
    lista["nome"] = str(input("nome do jogador: "))
    partidas = int(input(f"quantas partidas {lista["nome"]} jogou? "))
    for i in range(0, partidas):
        lista["gols"] = int(input(f"Na {i+1}° partida ele marcou: "))
        tot += (lista["gols"])
    lista["total"] = tot
    lista1.append(lista.copy())
    n = str(input("deseja continuar? ")).strip().lower()[0]
    while n not in "sn":
        n = str(input("deseja continuar? ")).strip().lower()[0]
print("")
print(f"{"NUM.":>2} // {"jogador":>5} //{"gols":>5}")
for k, c in enumerate(lista1):
    print(f"{k:>2} // {c["nome"]:>6} // {c["total"]:>5}")
 