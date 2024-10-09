lista = dict()
tot = 0
lista["nome"] = str(input("nome do jogador: "))
partidas = int(input(f"quantas partidas {lista["nome"]} jogou? "))
for i in range(0, partidas):
    lista["gols"] = int(input(f"Na {i+1}° partida ele marcou: "))
    tot += (lista["gols"])
print(f"O jogador {lista["nome"]} jogou {partidas} partidas.")
print(f"o total foi de {tot} gols")