from random import randint
comp = randint(0,10)
n = ()
cont = 0
while True:
    jogador = str(input("escolha entre PAR ou IMPAR? ")).lower().strip()
    j1 = int(input("escolha um numero entre 0 e 10: "))
    total = comp + j1
    print(total)
    if jogador == "impar":
        n == "par"
        if total % 2 != 0:
            print("voce venceu")
            cont += 1
        else:
            print("voce perdeu")
            b = str(input("deseja jogar novamente? [S/N] ")).lower().strip()
            if b == "s":
                cont = 0
                print("")
            else:
                break
    if jogador == "par":
        n == "impar"
        if total % 2 == 0:
            print(" voce venceu")
            cont += 1
        else:
            print("voce perdeu")
            b = str(input("deseja jogar novamente? [S/N] ")).lower().strip()
            if b == "s":
                cont = 0
                print("")
            else:
                break
print(f"vitorias consecutivas: {cont}")