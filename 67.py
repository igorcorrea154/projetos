print("TABUADA")
print("")
while True:
    n = int(input("digite um valor para ver sua tabuada: "))
    if n < 0:
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
print("PROGRAMA FINALIZADO, NAO FOI POSSIVEL FAZER A OPERACAO")