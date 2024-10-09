from random import randint
from operator import itemgetter
count = 1
lista = {"jogador 1": randint(1,6), "jogador 2": randint(1,6), "jogador 3": randint(1,6), "jogador 4": randint(1,6) }
for k, c in lista.items():
    print(f"o {k} tirou {c}")
rank = sorted(lista.items(),key=itemgetter(1), reverse=True)
print("")
print("Ranking dos jogadores:")
for v, c in rank:
    print(f"o {count}° foi: {v} que tirou {c}")
    count += 1
