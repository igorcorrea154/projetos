n = (int(input("digite um numero: ")),int(input("digite um numero: ")),int(input("digite um numero: ")),int(input("digite um numero: ")))
print(n)
print(f"o numero 9 apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"o numero 3 apareceu na {n.index(3)+1}º posicao")
else:
    print("o numero 3 não foi digitado")
print("os numeros pares foram: ")
for c in n:
    if c % 2 == 0:
        print(f"{c}")
