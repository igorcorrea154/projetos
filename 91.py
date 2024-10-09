def area():
    s = altura * largura
    print(f"a area de um terreno {altura}X{largura} = {s} m²")

print("CALCULAR AREA")
altura = float(input("ALTURA (m): "))
largura = float(input("LARGURA (m):  "))
area()