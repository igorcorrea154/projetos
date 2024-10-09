while True:
    data = int(input("digite a idade do competidor: "))
    idade = 2024 - data
    if idade <= 9:
        print("categoria MIRIM")
    elif idade > 9 and idade <= 14:
        print("categoria INFANTIL")
    elif idade > 14 and idade <= 19:
        print("categoria JUNIOR")
    elif idade > 19 and idade <= 20:
        print("categoria SENIOR")
    else:
        print("categoria MASTER")