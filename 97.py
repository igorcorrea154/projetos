def metade():
    met = valor / 2
    print(f"a metade de {valor} é igual a: {met}")
def dobro():
    dob = valor * 2
    print(f"o dobro de {valor} é igual a: {dob}")
def aumento10():
    aumento = (valor * 0.10) + valor
    print(f"aumentando 10% de {valor} é {aumento}")
def reducao13():
    reducao = valor - (valor * 0.13)
    print(f"reduzindo 13% de {valor} é {reducao}")
valor = float(input("R$"))
metade()
dobro()
aumento10()
reducao13()