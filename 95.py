def voto():
    from datetime import date
    data = int(input("digite o ano que voce nasceu: "))
    atual = date.today().year
    idade = atual - data
    print(f"com {idade} anos, o", end=" ")
    if idade < 18 and idade >= 16:
        print("VOTO É OPCIONAL")
    elif idade > 18 and idade < 65:
        print("VOTO É OBRIGATORIO")
    elif idade >= 65:
        print("VOTO É OPCIONAL")
    elif idade < 16:
        print("NAO É ELEGIVEL")

voto()