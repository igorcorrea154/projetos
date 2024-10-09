lista = list()
lista1 = list()
lista2 =  list()
sim = "s"
while sim in "s":
    lista.append(int(input("digite um valor: ")))
    sim = str(input("quer continuar? ")).strip().lower()[0]
for c in lista:
    if c % 2 == 0:
        lista1.append(c)
    else:
        lista2.append(c)
print(f"os numeros digitados foram: {lista}")
print(f"os numeros pares foram: {lista1}")
print(f"os numeros impares foram: {lista2}")