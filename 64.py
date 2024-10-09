n = int(input("digite um valor: "))
print("para parar basta digitar 999")
cont = 0
soma = n
while n != 999:
    
    n = int(input("digite outro valor: "))
    cont += 1
    if n == 999:
        break
    soma += n
print(f"a soma entre esses numeros foi de {soma} e foram calculados {cont} numeros")