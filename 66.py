cont = 0
soma = 0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"foram digitados {cont} numeros e a soma entre eles foi de {soma}")
