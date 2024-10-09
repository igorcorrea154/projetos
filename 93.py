def maior():
    numeros = list()
    ma = 0
    for c in range(1, 6):
        numero = int(input(f"digite um {c}° numero: "))
        numeros.append(numero)
        if c == 1:
            ma = numero
        else:
            if numero > ma:
                ma = numero
    print("foram digitados os numeros: ", end="")
    for num in numeros:
        print(f"{num}",end=", ")
    print(f"e o maior foi o {ma}")

maior()