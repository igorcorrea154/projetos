def calcular():
    binario = bin
    octal = oct
    hexadecimal = hex
    escolha = int(input("escolha um numero inteiro "))
    print("1- BINARIO ")
    print("2- OCTAL")
    print("3- HEXADECIMAL")
    e1 = int(input("escolha o metodo de conversao: "))
    if e1 == 1:
        print(f"o numero binario de {escolha} é {bin(escolha)}")
    elif e1 == 2:
        print(f"o numero octal de {escolha} é {oct(escolha)}")
    elif e1 == 3:
        print(f"o numero hexadecimal de {escolha} é {hex(escolha)}")

calcular()