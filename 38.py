def maior():
    n1 = int(input("escreva um numero inteiro: "))
    n2 = int(input("escreva outro numero inteiro: "))
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    elif n2 > n1:
        print(f"{n2} é maior que {n1}")
    else:
        print("os dois numeros sao iguais")
maior()