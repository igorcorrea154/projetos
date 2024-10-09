n = "s"
cont1 = 0
cont2 = 0
cont3 = 0
while n == "s":
    print("-"*30)
    idade = int(input("qual a idade dessa pessoa? "))
    sexo = str(input("qual o sexo dessa pessoa? [M/F]: ")).lower().strip()[0]
    print("-"*30)
    n = str(input("QUER CONTINUAR? [S/N]: ")).lower().strip()[0]
    if sexo == "m":
        cont3 += 1
    if idade > 18:
        cont1 += 1
    if sexo == "f":
        if idade < 20:
            cont2 += 1
print("")
print(f"{cont1} pessoas tem mais de 18 anos, {cont2} mulheres tem menos de 20 anos, foram cadastrados {cont3} homens")