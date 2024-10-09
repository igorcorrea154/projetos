from random import choice
while True:
    n1 = ["pedra", "papel", "tesoura"]
    n2 = choice(n1)
    print("JOKEMPO")
    jokempo = str(input("escolha pedra, papel ou tesoura: ").lower()).strip()[1]
    if jokempo == "pedra":
        if n2 == "pedra":
            print("EMPATE!!!")
        elif n2 == "tesoura":
            print("a pedra amassou a {}. VOCE GANHOU !!!".format(n2))
        else:
            print("o {} embrulhou a pedra. VOCE PERDEU!!!".format(n2))
    elif jokempo == "papel":
        if n2 == "papel":
            print("EMPATE!!!")
        elif n2 == "pedra":
            print("o papel embrulhou a {}, VOCE GANHOU!!!".format(n2))
        else:
            print("a {} cortou o papel. VOCE PERDEU!!!".format(n2))
    else:
        if n2 == "tesoura":
            print("EMPATE!!!")
        elif n2 == "papel":
            print("a tesoura cortou o {}, VOCE GANHOU!!!".format(n2))
        else:
            print("a {} quebrou a tesoura, VOCE PERDEU!!!!".format(n2))