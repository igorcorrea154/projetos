lista = list()
count = 0
n = "s"
while n in "s":
    lista.append(int(input("digite um numero: ")))
    n = str(input("deseja continuar? ")).lower().strip()[0]
    count += 1
lista.sort(reverse = True)
if 5 in lista:
    print("o numero 5 esta na lista")
else:
    print(" o numero 5 nao se encontra na lista")
print(f"foram digitados {count} elementos")
print(f"a ordem decrescente deles é {lista}")